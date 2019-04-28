FROM eltonlaw/pybase

COPY ./requirements /impyute/requirements
RUN pip2.7 install -r /impyute/requirements/dev.txt && \
    pip3.5 install -r /impyute/requirements/dev.txt && \
    pip3.6 install -r /impyute/requirements/dev.txt && \
    pip3.7 install -r /impyute/requirements/dev.txt

COPY ./setup.py ./setup.cfg ./README.rst /impyute/
COPY ./docs /impyute/docs
COPY ./test/ /impyute/test
COPY ./impyute /impyute/impyute
WORKDIR /impyute
RUN pip2.7 install -e . && \
    pip3.5 install -e . && \
    pip3.6 install -e . && \
    pip3.7 install -e .

CMD ["python3.6", "-m", "pytest"]
