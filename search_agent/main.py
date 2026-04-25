import asyncio
from google.adk import Agent, Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

# -- Definindo o agente -- #
agent = Agent(
    name="search",
    model="gemini-2.5-flash",
    instruction="Responda as perguntas"
)

# -- Iniciando a Sessão --#
session_service = InMemorySessionService()

# -- Definindo a sessão --#
async def setup_session():
    session_id = "session-123"
    user_id = "me"
    app_name = "search"

    #aqui é importante ser assíncrono
    await session_service.create_session(
        app_name=app_name,
        user_id=user_id,
        session_id=session_id,
    )
    return session_id, user_id, app_name

# --Definindo o Runner(como o agente será chamado) --#
async def call_agent(query: str, session_id: str, user_id: str, app_name: str):
    content = types.Content(
        role="user",
        parts=[types.Part(text=query)]
    )
    runner = Runner(
        agent=agent,
        app_name=app_name,
        session_service=session_service
    )

    async for event in runner.run_async(
        user_id=user_id,
        session_id=session_id,
        new_message=content
    ):
        if event.is_final_response():
            print("Resposta:", event.content.parts[0].text)

# --Initialize party-- #
async def main():
    session_id, user_id, app_name = await setup_session()
    await call_agent("Explique o que é Python.", session_id, user_id, app_name)

if __name__ == "__main__":
    asyncio.run(main())