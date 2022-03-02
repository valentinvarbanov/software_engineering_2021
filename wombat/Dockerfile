FROM python:3.8 
# COPY ../requirements.txt /wombat
COPY . /wombat
WORKDIR /wombat
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["python","manage.py","runserver", "0.0.0.0:8000"] 