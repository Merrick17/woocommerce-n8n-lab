FROM wordpress:cli

USER root
RUN apk add --no-cache curl
COPY bootstrap.sh /bootstrap.sh
RUN sed -i 's/\r$//' /bootstrap.sh && chmod +x /bootstrap.sh
USER www-data

ENTRYPOINT ["/bin/sh", "/bootstrap.sh"]
