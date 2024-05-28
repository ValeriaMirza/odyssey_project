import unittest
from data_processing import extract_movie_type, extract_duration_period, extract_name, extract_genre

class TestMovieDataExtraction(unittest.TestCase):

    def test_extract_movie_type(self):
        """Function for testing the extract_movie_type function"""
        self.assertEqual(extract_movie_type('Poveste din cartierul de vestPG-132\xa0h 36\xa0min.De comedie'), 'PG-13')
        self.assertEqual(extract_movie_type('DunePG-132\xa0h 35\xa0min.Acțiune'), 'PG-13')
        self.assertEqual(extract_movie_type('În ghearele câinilorR2\xa0h 5\xa0min.Dragoste'), 'R')

    def test_extract_duration_period(self):
        """Function for testing the extract_duration_period function"""
        self.assertEqual(extract_duration_period('Poveste din cartierul de vestPG-132\xa0h 36\xa0min.De comedie'), (2, 36))
        self.assertEqual(extract_duration_period('DunePG-132\xa0h 35\xa0min.Acțiune'), (2,35))
        self.assertEqual(extract_duration_period('În ghearele câinilorR2\xa0h 5\xa0min.Dragoste'), (2, 5))
    

    def test_extract_name(self):
        """Function for testing the extract_name function"""
        self.assertEqual(extract_name('Poveste din cartierul de vestPG-132\xa0h 36\xa0min.De comedie', 'PG-13'), 'Poveste din cartierul de vest')
        self.assertEqual(extract_name('DunePG-132\xa0h 35\xa0min.Acțiune'), 'Dune')
        self.assertEqual(extract_name('În ghearele câinilorR2\xa0h 5\xa0min.Dragoste', 'R'), 'În ghearele câinilor')
        

    def test_extract_genre(self):
        """Function for testing the extract_genre function"""
        self.assertEqual(extract_genre('Poveste din cartierul de vestPG-132\xa0h 36\xa0min.De comedie'), 'De comedie')
        self.assertEqual(extract_genre('DunePG-132\xa0h 35\xa0min.Acțiune'), 'Acțiune')
        self.assertEqual(extract_genre('În ghearele câinilorR2\xa0h 5\xa0min.Dragoste'), 'Dragoste')
    

if __name__ == '__main__':
    unittest.main()
