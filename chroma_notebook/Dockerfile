FROM jupyter/base-notebook:latest

USER root
RUN pip install --no-cache-dir chromadb && pip install --no-cache-dir python-decouple && pip install --no-cache-dir google-adk

USER ${NB_UID}
RUN jupyter notebook --generate-config --allow-root
RUN echo "c.NotebookApp.token = ''" >> ~/.jupyter/jupyter_notebook_config.py
RUN echo "c.NotebookApp.password = ''" >> ~/.jupyter/jupyter_notebook_config.py
RUN echo "c.NotebookApp.ip = '0.0.0.0'" >> ~/.jupyter/jupyter_notebook_config.py
RUN echo "c.NotebookApp.port = 8888" >> ~/.jupyter/jupyter_notebook_config.py
RUN echo "c.NotebookApp.open_browser = False" >> ~/.jupyter/jupyter_notebook_config.py
RUN echo "c.NotebookApp.allow_root = True" >> ~/.jupyter/jupyter_notebook_config.py

EXPOSE 8888
CMD ["start-notebook.sh"]