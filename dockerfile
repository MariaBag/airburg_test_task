FROM python:3.12

# Security updates & Update pip and setuptools
RUN apt-get -y update \
    && apt-get -y upgrade \
    && python -m pip install --upgrade pip setuptools \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /airburg_test_task

# Install python requirements
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy app-related files
COPY test_task ./

# Copy manage.py
COPY test_task/manage.py ./test_task

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

EXPOSE 8000
