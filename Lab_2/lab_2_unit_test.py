import unittest

class TestFrequencyTable(unittest.TestCase):
        
    def setUp(self):
        self.table = [
        345.1, 261.8, 292.4, 326.4, 396.1, 307.7, 372.3,
        260.1, 285.6, 224.4, 346.8, 280.5, 334.9, 348.5,
        243.1, 341.7, 285.6, 249.9, 353.6, 331.5, 260.1,
        328.1, 302.6, 275.4, 266.9, 387.6, 372.3, 212.5,
        171.7, 358.7, 311.1, 249.9, 246.5, 307.7, 312.8,
        236.3, 324.7, 314.5, 343.4, 404.6, 283.9, 346.8,
        331.5, 292.4, 333.2, 234.6, 362.1, 297.5, 329.8,
        302.6, 229.5, 302.6, 200.6, 316.2, 324.7, 331.5 ]
        self.interval_count = 7
        
    def test_min_val(self):
        self.assertEqual(min(self.table), 171.7)
        
    def test_max_val(self):
        self.assertEqual(max(self.table), 404.6)
        
    def test_interval_width(self):
        min_val = min(self.table)
        max_val = max(self.table)
        interval_width = (max_val - min_val) / self.interval_count
        self.assertEqual(interval_width, 33.27142857142858)
        
    def test_intervals(self):
        min_val = min(self.table)
        max_val = max(self.table)
        interval_width = (max_val - min_val) / self.interval_count
        intervals = []
        for i in range(self.interval_count):
            intervals.append([min_val + i * interval_width, min_val + (i + 1) * interval_width])
            
        expected_intervals = [ [171.7   , 204.97142857142856],                  
                    [204.97142857142856, 238.24285714285713],                
                    [238.24285714285713, 271.51428571428573],                
                    [271.51428571428573, 304.78571428571433],                
                    [304.78571428571433, 338.0571428571429],                
                    [338.0571428571429, 371.3285714285715],                 
                    [371.3285714285715, 404.6] ]
        self.assertEqual(intervals, expected_intervals)
        
    def test_intervals_mid(self):
        min_val = min(self.table)
        max_val = max(self.table)
        interval_width = (max_val - min_val) / self.interval_count
        intervals = []
        for i in range(self.interval_count):
            intervals.append([min_val + i * interval_width, min_val + (i + 1) * interval_width])
            
        intervals_mid = []
        for interval in intervals:
            intervals_mid.append((interval[0] + interval[1]) / 2)
            
        expected_intervals_mid = [ 188.3357142857143, 221.60714285714283,
                                    254.87857142857143, 288.15000000000003,  	                 
                                    321.4214285714286, 354.6928571428572,  	                 
                                    387.9642857142858 ]
        self.assertListEqual(intervals_mid, expected_intervals_mid)
        
    def test_frequencies(self):
        min_val = min(self.table)
        max_val = max(self.table)
        interval_width = (max_val - min_val) / self.interval_count
        intervals = []
        for i in range(self.interval_count):
            intervals.append([min_val + i * interval_width, min_val + (i + 1) * interval_width])
            
        intervals_mid = []
        for interval in intervals:
            intervals_mid.append((interval[0] + interval[1]) / 2)
            
        frequencies = [0] * self.interval_count
        for val in self.table:
            for i in range(self.interval_count):
                if val >= intervals[i][0] and val < intervals[i][1]:
                    frequencies[i] += 1
                    break
                
        expected_frequencies = [ 2, 5, 8, 11, 16, 9, 4 ]
        for i in range(self.interval_count):
            with self.subTest(i=i):
                self.assertEqual(frequencies[i], expected_frequencies[i])
                
                
if __name__ == "__main__":
    unittest.main()