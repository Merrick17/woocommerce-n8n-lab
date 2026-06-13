FROM n8nio/n8n

USER root
COPY docker-entrypoint.sh /docker-entrypoint.sh
COPY credentials.json workflow.json /bootstrap/
RUN sed -i 's/\r$//' /docker-entrypoint.sh && chmod +x /docker-entrypoint.sh
USER node

ENTRYPOINT ["/docker-entrypoint.sh"]
