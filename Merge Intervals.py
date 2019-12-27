class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals = sorted(intervals, key=lambda x:x[0])
        
        final_list = []
        
        for i in range(len(intervals)):
            
            if len(final_list)==0:
                final_list.append(intervals[i])
                continue
            
            if final_list[-1][1]>=intervals[i][0]:
                
                if final_list[-1][1]>=intervals[i][1]:
                    continue
                    
                else:
                    final_list[-1][1]=intervals[i][1]
                    continue
            else:
                final_list.append(intervals[i])
        
        return final_list
        