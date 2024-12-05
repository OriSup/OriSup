
FROM python:3.11-slim 

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


WORKDIR /app


COPY . /app


RUN pip install --no-cache-dir streamlit python-dotenv


RUN apt-get update && apt-get install -y \
    python3 && \
    apt-get clean


EXPOSE 8501 8000


RUN echo '#!/bin/bash\n\
python3 -m http.server 8000 --directory /app/landingpage &\n\
streamlit run /app/streamlit_app.py\n' > /app/start.sh && chmod +x /app/start.sh


ENTRYPOINT ["/bin/bash", "/app/start.sh"]
