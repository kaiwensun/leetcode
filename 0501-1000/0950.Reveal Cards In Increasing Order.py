class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        ordered = sorted(deck)
        rval = [0] * len(ordered)
        picker = 0
        start = 0
        step = 2
        top_is_skipped = False
        while picker < len(ordered):
            for i in xrange(start, len(rval), step):
                rval[i] = ordered[picker]
                picker += 1
            should_skip_top = i + step / 2 >= len(ordered)
            if top_is_skipped:
                start -= step / 2
            else:
                start += step / 2
            if should_skip_top:
                start += step
                if start >= len(ordered):
                    start -= step
            step += step
            top_is_skipped = should_skip_top
        return rval
