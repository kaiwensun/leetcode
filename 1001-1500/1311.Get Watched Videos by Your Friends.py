from collections import Counter
class Solution(object):
    def watchedVideosByFriends(self, watchedVideos, friends, id, level):
        """
        :type watchedVideos: List[List[str]]
        :type friends: List[List[int]]
        :type id: int
        :type level: int
        :rtype: List[str]
        """
        friends = map(set, friends)
        visited = {id}
        currs = {id}
        for i in xrange(level):
            nxt = set()
            for fid in currs:
                nxt |= friends[fid] - visited
            currs = nxt
            visited |= currs
        cnt = Counter()
        for fid in currs:
            for v in watchedVideos[fid]:
                cnt[v] += 1
        return map(lambda (count, video): video, sorted((count, video) for video, count in cnt.iteritems()))
