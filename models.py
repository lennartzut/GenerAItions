from extensions import db


class Individual(db.Model):
    __tablename__ = 'individuals'

    id = db.Column(db.Integer, primary_key=True)
    birth_date = db.Column(db.Date, nullable=True)
    birth_place = db.Column(db.String(100), nullable=True)
    death_date = db.Column(db.Date, nullable=True)
    death_place = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return f'<Individual id={self.id}, birth_place={self.birth_place}>'

