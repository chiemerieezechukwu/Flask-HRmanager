from flask import abort, session, redirect, url_for
from functools import wraps
from coolhr.models import Companies, Employees


# add a functionality that takes them to the page they initially tried to visit if they are logged in correctly
def access_company(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        if not (session.get("company_email") or session.get("employee_email")):
            return redirect(url_for("company_username"))
        company = Companies.query.filter_by(
            company_email=session.get("company_email"),
            company_username=kwargs["company_username"],
        ).first()
        if company is None:
            abort(403)
        return function(*args, **kwargs)

    return wrapper


def access_employee(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        if not (session.get("company_email") or session.get("employee_email")):
            return redirect(url_for("company_username"))
        employee = Employees.query.filter_by(
            employee_email=session.get("employee_email")
        ).first()
        if employee is None:
            abort(403)
        e_company = Companies.query.filter_by(company_id=employee.company_id).first()
        if e_company.company_username != kwargs["company_username"]:
            abort(403)
        return function(*args, **kwargs)

    return wrapper
