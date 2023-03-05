FROM python:3.8

RUN pip3 install --upgrade pip

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN useradd --create-home --shell /bin/bash blog_user
WORKDIR /blog_app
RUN chown -R blog_user:blog_user /blog_app

USER blog_user

COPY --chown=blog_user:blog_user requirements.txt requirements.txt
RUN pip3 install --user -r requirements.txt



COPY --chown=blog_user:blog_user . . 

CMD python manage.py runserver 0.0.0.0:8000