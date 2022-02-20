from flask_app.config.mysqlconnection import connectToMySQL
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

from flask import flash

class Email:
    def __init__(self,data):
        self.id = data['id']

        self.email_address = data['email_address']
        self.created_at = data['created_at']
        self.update_at = data['updated_at']

#=======================================================================
# displays all of the emails in the db on assigned page
    @classmethod
    def allEmails(cls):
        query = "SELECT * FROM emails;"
        results = connectToMySQL("emails_schema").query_db(query)

        allEmails= []

        for emails in results:
            allEmails.append(cls(emails))

        return allEmails
#=======================================================================

#=======================================================================
# Save creating email
    @classmethod
    def save(cls,data):
        query = "INSERT INTO emails(email_address, created_at) VALUES(%(email_address)s, NOW());"
        email_address = connectToMySQL("emails_schema").query_db(query, data)
        return email_address
#=======================================================================

#=======================================================================
#Validating the email submission STATICMETHOD

    @staticmethod
    def is_valid(email_address):
        is_valid = True

        query = "SELECT * FROM emails WHERE email_address = %(email_address)s;"
        email_address = connectToMySQL("emails_schema").query_db(query, email_address)

        if len(email_address) >= 1:
            is_valid = False
            flash("Email is already taken")

        return is_valid
#=======================================================================
