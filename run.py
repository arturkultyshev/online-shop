from e_shop import app
import os


if __name__ =="__main__":
    port = int(os.environ.get("PORT", 5050))
    app.run(port=port, host='0.0.0.0')