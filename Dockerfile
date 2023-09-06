FROM python:3.8
WORKDIR SDE_Intern/app.py
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
CMD ["python",",appy.py"]