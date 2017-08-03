from flask_sqlalchemy import SQLAlchemy
from app import app

db = SQLAlchemy(app)


class food_desc(db.Model):
    __tablename__ = 'food_description'

    food_id = db.Column(db.Integer(), primary_key=True)
    ndbno_id = db.Column(db.String())
    short_desc = db.Column(db.String())
    food_cat = db.Column(db.String())

    def __init__(self, ndbno_id, short_desc, food_cat):
        self.ndbno_id = ndbno_id
        self.short_desc = short_desc
        self.food_cat = food_cat

    def __repr__(self):
        return '<id {}>'.format(self.food_id)


class food_units(db.Model):
    __tablename__ = 'food_units'

    food_id = db.Column(db.String(), primary_key=True)
    unit_desc = db.Column(db, String())
    grams_per_unit = db.Column(db.Float)

    def __init__(self, food_id, unit_desc, grams_per_unit):
        self.food_id = food_id
        self.unit_desc = unit_desc
        self.grams_per_unit = grams_per_unit

    def __repr__(self):
        return '<id {}>'.format(self.food_id)


class nut_per_100_g(db.Model):
    __tablename__ = 'nutients_per_100_grams'

    food_id = db.Column(db.String())
    kcal = db.Column(db.Float)
    protein_g = db.Column(db.Float)
    total_fat_g = db.Column(db.Float)
    total_carb_g = db.Column(db.Float)
    total_diet_fiber_g = db.Column(db.Float)
    calcium_mg = db.Column(db.Float)
    iron_mg = db.Column(db.Float)
    magnesium_mg = db.Column(db.Float)
    phosphorus_mg = db.Column(db.Float)
    potassium_mg = db.Column(db.Float)
    sodium_mg = db.Column(db.Float)
    zinc_mg = db.Column(db.Float)
    copper_mg = db.Column(db.Float)
    manganese_mg = db.Column(db.Float)
    selenium_mcg = db.Column(db.Float)
    vitamin_c_mg = db.Column(db.Float)
    thiamin_mg = db.Column(db.Float)
    riboflavin_mg = db.Column(db.Float)
    niacin_mg = db.Column(db.Float)
    pantothenic_acid_mg = db.Column(db.Float)
    vitamin_b6_mg = db.Column(db.Float)
    total_folate_mcg = db.Column(db.Float)
    vitamin_b12_mcg = db.Column(db.Float)
    vitamin_d_mcg = db.Column(db.Float)
    vitamin_e_mg = db.Column(db.Float)
    vitamin_k_mcg = db.Column(db.Float)
    total_sat_fat_g = db.Column(db.Float)
    total_monounsat_fat_g = db.Column(db.Float)
    total_poly_unsat_fat_g = db.Column(db.Float)
    total_trans_fat_g = db.Column(db.Float)
    cholesterol_mg = db.Column(db.Float)
    total_sugar_g = db.Column(db.Float)
    omega_3_fatty_acids_g = db.Column(db.Float)

    def __init__(self, food_id, kcal, protein_g, total_fat_g, total_carb_g,
                 total_diet_fiber_g, calcium_mg, iron_mg, magnesium_mg,
                 phosphorus_mg, potassium_mg, sodium_mg, zinc_mg, copper_mg,
                 manganese_mg, selenium_mcg, vitamin_c_mg, thiamin_mg,
                 riboflavin_mg,
                 niacin_mg, pantothenic_acid_mg, vitamin_b6_mg,
                 total_folate_mg,
                 vitamin_b12_mcg, vitamin_d_mcg, vitamin_e_mg, vitamin_k_mcg,
                 total_sat_fat_g, total_monounsat_fat_g,
                 total_poly_insat_fat_g,
                 total_trans_fat_g, cholesterol_mg, total_sugar_g,
                 omega_3_fatty_acids_g):
        self.food_id = food_id
        self.kcal = kcal
        self.protein_g = protein_g
        self.total_fat_g = total_fat_g
        self.total_carb_g = total_carb_g
        self.total_diet_fiber_g = total_diet_fiber_g
        self.calcium_mg = calcium_mg
        self.iron_mg = iron_mg
        self.magnesium_mg = magnesium_mg
        self.phosphorus_mg = phosphorus_mg
        self.potassium_mg = potassium_mg
        self.sodium_mg = sodium_mg
        self.zinc_mg = zinc_mg
        self.copper_mg = copper_mg
        self.manganese_mg = manganese_mg
        self.selenium_mcg = selenium_mcg
        self.vitamin_c_mg = vitamin_c_mg
        self.thiamin_mg = thiamin_mg
        self.riboflavin_mg = riboflavin_mg
        self.niacin_mg = niacin_mg
        self.pantothenic_acid_mg = pantothenic_acid_mg
        self.vitamin_b6_mg = vitamin_b6_mg
        self.total_folate_mcg = total_folate_mcg
        self.vitamin_b12_mcg = vitamin_b12_mcg
        self.vitamin_d_mcg = vitamin_d_mcg
        self.vitamin_e_mg = vitamin_e_mg
        self.vitamin_k_mcg = vitamin_k_mcg
        self.total_sat_fat_g = total_sat_fat_g
        self.total_monounsat_fat_g = total_monounsat_fat_g
        self.total_poly_unsat_fat_g = total_poly_unsat_fat_g
        self.total_trans_fat_g = total_trans_fat_g
        self.cholesterol_mg = cholesterol_mg
        self.total_sugar_g = total_sugar_g
        self.omega_3_fatty_acids_g = omega_3_fatty_acids_g

    def __repr__(self):
        return '<id {}>'.format(self.food_id)


class food_upc(db.Model):
    __tablename__ = 'food_upc'

    food_id = db.Column(db.Integer, primary_key=True)
    food_upc = db.Column(db.String())

    def __init__(self, food_id, food_upc):
        self.food_id = food_id
        self.food_upc = food_upc

    def __repr__(self):
        return '<id {}>'.format(self.food_id)
