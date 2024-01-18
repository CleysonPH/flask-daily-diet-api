from dailydiet.ext.database import db


class Meal(db.Model):
    __tablename__ = "meals"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text)
    datetime = db.Column(db.DateTime, nullable=False)
    in_diet = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, name, description, datetime, in_diet=False):
        self.name = name
        self.description = description
        self.datetime = datetime
        self.in_diet = in_diet

    def __repr__(self):
        return f"<Meal {self.id}>"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "datetime": self.datetime.isoformat(),
            "in_diet": self.in_diet,
        }
