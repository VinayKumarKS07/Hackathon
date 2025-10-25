from flask import Flask
from flask_restful import Api , Resource
from db import db
from config import Config
from resources.CustomerResource import CustomerResource
from resources.AccountResource import AccountResource

app=Flask(__name__);
app.config.from_object(Config)
api=Api(app);
db.init_app(app);

api.add_resource(
    CustomerResource,
    '/customers',
    '/customers/id/<string:customer_id>',
    '/customers/email/<string:email>'
)
api.add_resource(
    AccountResource,
    '/api/accountcreation',
    '/accounts/<string:account_number>'
)

if __name__ == '__main__':
    app.run(debug=True)

