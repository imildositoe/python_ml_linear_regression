import numpy as np
import pandas as pd
from sqlalchemy import create_engine, Column, Integer, Float, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
# from sqlalchemy.ext.declarative import declarative_base
from bokeh.plotting import figure, show, output_file
import os

# Define the SQLAlchemy Base
Base = declarative_base()

# Define TrainingData table class
class TrainingData(Base):
    __tablename__ = 'training_data'
    id = Column(Integer, primary_key=True)
    x = Column(Float)
    y1 = Column(Float)
    y2 = Column(Float)
    y3 = Column(Float)
    y4 = Column(Float)

# Define IdealFunctions table class
class IdealFunctions(Base):
    __tablename__ = 'ideal_functions'
    id = Column(Integer, primary_key=True)
    x = Column(Float)
    y1 = Column(Float)
    y2 = Column(Float)
    # Add columns for y3 to y50 as needed...

# Define TestData table class
class TestData(Base):
    __tablename__ = 'test_data'
    id = Column(Integer, primary_key=True)
    x = Column(Float)
    y = Column(Float)
    ideal_func = Column(Integer)
    deviation = Column(Float)

# Main class for data processing
class DataProcessor:
    def __init__(self, db_path):
        self.engine = create_engine(f'sqlite:///{db_path}')
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def load_training_data(self, file_path):
        session = self.Session()
        train_df = pd.read_csv(file_path)
        train_df.to_sql('training_data', self.engine, if_exists='replace', index=False)
        session.commit()
        session.close()

    def load_ideal_functions(self, file_path):
        session = self.Session()
        ideal_df = pd.read_csv(file_path)
        ideal_df.to_sql('ideal_functions', self.engine, if_exists='replace', index=False)
        session.commit()
        session.close()

    def load_test_data(self, file_path):
        session = self.Session()
        test_df = pd.read_csv(file_path)
        for _, row in test_df.iterrows():
            x_val, y_val = row['x'], row['y']
            session.execute(f"INSERT INTO test_data (x, y) VALUES ({x_val}, {y_val})")
        session.commit()
        session.close()

    def match_and_calculate_deviations(self):
        session = self.Session()
        test_data = session.query(TestData).all()
        for data_point in test_data:
            x_val, y_val = data_point.x, data_point.y
            min_deviation = float('inf')
            assigned_function = None
            for ideal_func in session.query(IdealFunctions).all():
                deviation = np.sqrt((y_val - ideal_func.y1) ** 2)
                if deviation < min_deviation and deviation <= np.sqrt(2) * np.max([ideal_func.y1, ideal_func.y2, ideal_func.y3, ideal_func.y4]):
                    min_deviation = deviation
                    assigned_function = ideal_func.id
            data_point.ideal_func = assigned_function
            data_point.deviation = min_deviation
        session.commit()
        session.close()

    def visualize_data(self):
        session = self.Session()
        test_data = session.query(TestData).all()

        p = figure(title="Data Visualization", x_axis_label="x", y_axis_label="y")
        color_list = ["blue", "green", "red", "purple"]

        for func_id in range(1, 5):
            ideal_func = session.query(IdealFunctions).filter_by(id=func_id).first()
            p.line(ideal_func.x, ideal_func.y1, line_width=2, line_color=color_list[func_id - 1], legend_label=f"Ideal Function {func_id}")

        for data_point in test_data:
            if data_point.ideal_func is not None:
                p.circle(data_point.x, data_point.y, size=8, color=color_list[data_point.ideal_func - 1], legend_label=f"Test Data (Deviation: {data_point.deviation:.2f})")

        output_file("visualization.html")
        show(p)

# Main program
if __name__ == "__main__":
    db_path = 'data.db'
    processor = DataProcessor(db_path)

    # Load training data, ideal functions, and test data
    processor.load_training_data('train.csv')
    processor.load_ideal_functions('ideal.csv')
    processor.load_test_data('test.csv')

    # Match test data to ideal functions and calculate deviations
    processor.match_and_calculate_deviations()

    # Visualize the data
    processor.visualize_data()
76, 64, 67, 79