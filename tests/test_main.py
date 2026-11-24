import unittest
from main import analyze_job, load_jobs, summarize


class TestAnalyzer(unittest.TestCase):
    def test_success(self):
        self.assertIsNone(analyze_job({'job':'ok','status':'DONE','duration_minutes':'10','expected_minutes':'10'}))

    def test_error(self):
        self.assertIn('status ERROR', analyze_job({'job':'bad','status':'ERROR','duration_minutes':'0','expected_minutes':'10'}))

    def test_slow(self):
        self.assertIn('31 min', analyze_job({'job':'slow','status':'DONE','duration_minutes':'31','expected_minutes':'10'}))

    def test_exact_limit_is_normal(self):
        self.assertIsNone(analyze_job({'job':'limit','status':'DONE','duration_minutes':'20','expected_minutes':'10'}))

    def test_sample(self):
        result = summarize(load_jobs('samples/execucoes.csv'))
        self.assertEqual((result['total'],result['normal'],len(result['alerts'])),(5,2,3))

    def test_invalid_duration(self):
        with self.assertRaises(ValueError):
            analyze_job({'job':'bad','status':'DONE','duration_minutes':'xyz','expected_minutes':'10'})

if __name__ == '__main__':
    unittest.main()
