import sys
import logging
logging.basicConfig(
        level=logging.DEBUG,
        style='{',
        format="{asctime} [{levelname}] {filename}:{lineno} {funcName} - {message}",
        stream=sys.stderr,
        )
import app
app.application.run(port=8080, trace=True)
