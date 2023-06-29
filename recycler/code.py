import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from bokeh.plotting import figure, show
from bokeh.io import output_file

Base = declarative_base()
engine = create_engine('sqlite:///data.db')
Session = sessionmaker(bind=engine)
session = Session()

class TrainingData(Base):
    __tablename__ = 'training_data'
    id = Column(Integer, primary_key=True)
    x = Column(Float)
    y1 = Column(Float)
    y2 = Column(Float)
    y3 = Column(Float)
    y4 = Column(Float)

class IdealFunctions(Base):
    __tablename__ = 'ideal_functions'
    id = Column(Integer, primary_key=True)
    x = Column(Float)
    y1 = Column(Float)
    y2 = Column(Float)
    y3 = Column(Float)
    y4 = Column(Float)
    # ... continue for all 51 columns

class TestData(Base):
    __tablename__ = 'test_data'
    id = Column(Integer, primary_key=True)
    x = Column(Float)
    y = Column(Float)
    ideal_function = Column(String)
    deviation = Column(Float)

class DatabaseManager:
    def __init__(self, db_name):
        self.db_name = db_name
    
    def create_tables(self):
        Base.metadata.create_all(engine)
    
    def load_training_data(self, file_path):
        # Load the training data from CSV file and populate the training_data table
    
        def load_ideal_functions(self, file_path):
            # Load the ideal functions from CSV file and populate the ideal_functions table
        
            def load_test_data(self, file_path):
                # Load the test data from CSV file, match it with ideal functions, and populate the test_data table
                
                def visualize_deviation(self):
                    # Visualize the deviation using Bokeh
                    
                    def close_connection(self):
                        session.close()


class CustomException(Exception):
    pass

# Unit tests

def test_load_training_data():
    pass

def test_load_ideal_functions():
    pass

def test_load_test_data():
    pass

def test_visualize_deviation():
    pass

if __name__ == '__main__':
    db_manager = DatabaseManager('data.db')
    db_manager.create_tables()
    db_manager.load_training_data('training_data.csv')
    db_manager.load_ideal_functions('ideal_functions.csv')
    db_manager.load_test_data('test_data.csv')
    db_manager.visualize_deviation()
    db_manager.close_connection()
