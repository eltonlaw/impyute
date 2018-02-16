FROM python:3.6

COPY ./requirements /requirements
RUN pip install -r /requirements/test.txt

COPY ./impyute /impyute
COPY ./test /impyute/test
WORKDIR /impyute

CMD ["pytest"]
