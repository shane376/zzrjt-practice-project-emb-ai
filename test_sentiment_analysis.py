from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
import unittest

#Testing class for sentiment_analyzer
class TestSentimentAnalyzer(unittest.Testcase):
    def test_sentiment_analyzer(self):
        #Test positive case
        result_1 = sentiment_analyzer("I love working with Python")
        self.assertEqual(result_1['label'], 'SENT_POSITIVE')
        #Test negative case
        result_2 = sentiment_analyzer("I hate working with Python")
        self.assertEqual(result_2['label'], 'SENT_NEGATIVE')
        #Test neutral case
        result_3 = sentiment_analyzer("I am neutral on Python")
        self.assertEqual(result_3['label'], "SENT_NEUTRAL")

#Call unit tests
unittest.main()