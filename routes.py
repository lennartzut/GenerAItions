from flask import Blueprint, request, jsonify
from models import Individual
from extensions import db
from schemas import IndividualSchema

api = Blueprint('api', __name__)

# Marshmallow schemas
individual_schema = IndividualSchema()
individuals_schema = IndividualSchema(many=True)


# Create Individual
@api.route('/individuals', methods=['POST'])
def create_individual():
    data = request.json
    try:
        individual = individual_schema.load(data)
        db.session.add(individual)
        db.session.commit()
        return jsonify({'id': individual.id,
                        'message': 'Individual created'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400


# Get All Individuals
@api.route('/individuals', methods=['GET'])
def get_individuals():
    individuals = Individual.query.all()
    return jsonify(individuals_schema.dump(individuals)), 200


# Get Individual by ID
@api.route('/individuals/<int:id>', methods=['GET'])
def get_individual(id):
    individual = Individual.query.get_or_404(id)
    return jsonify(individual_schema.dump(individual)), 200


# Update Individual
@api.route('/individuals/<int:id>', methods=['PUT'])
def update_individual(id):
    data = request.json
    individual = Individual.query.get_or_404(id)
    try:
        for key, value in data.items():
            setattr(individual, key, value)
        db.session.commit()
        return jsonify(
            {'message': 'Individual updated successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


# Delete Individual
@api.route('/individuals/<int:id>', methods=['DELETE'])
def delete_individual(id):
    individual = Individual.query.get_or_404(id)
    db.session.delete(individual)
    db.session.commit()
    return jsonify(
        {'message': 'Individual deleted successfully'}), 200
