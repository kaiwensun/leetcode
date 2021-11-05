class Solution:
    def countCombinations(self, pieces: List[str], positions: List[List[int]]) -> int:
        N = len(pieces)
        BOARD_SIZE = 8
        POSITIONS = [x - 1 + y * 1j - 1j for x, y in positions]

        def get_step_generator(i):
            ROOK = [1, -1, 1j, -1j]
            BISHOP = [1 + 1j, 1 - 1j, 1j - 1, -1 - 1j]
            QUEEN = BISHOP + ROOK
            DELTAS = {
                'rook': ROOK, 'bishop': BISHOP, 'queen': QUEEN
            }
            DELTA = DELTAS[pieces[i]]
            yield 0, 1
            for delta in DELTA:
                for move in range(1, BOARD_SIZE + 1):
                    target = POSITIONS[i] + delta * move
                    if not (0 <= target.real < BOARD_SIZE and 0 <= target.imag < BOARD_SIZE):
                        break
                    yield delta, move

        def simulate_steps(steps):
            """
            Each `steps` describes one snapshot of the final positions of all pieces.
            `simulate_steps` checks whether the snapshot is valid.
            """
            cur = list(POSITIONS)
            max_move = max(move for delta, move in steps)
            for cur_move in range(max_move):
                for i in range(N):
                    delta, move = steps[i]
                    if cur_move < move:
                        cur[i] += delta
                if len(set(cur)) != N:
                    return 0  # collide, but can possibly go further
            return 1 # valid

        N = len(pieces)
        step_generators = [get_step_generator(i) for i in range(N)]
        i = 0
        steps = [next(step_generator) for step_generator in step_generators]
        res = 0
        while True:
            rtn = simulate_steps(steps)
            res += rtn
            steps[i] = next(step_generators[i], None)
            while steps[i] == None:
                step_generators[i] = get_step_generator(i)
                steps[i] = next(step_generators[i])
                i += 1
                if i == N:
                    return res
                steps[i] = next(step_generators[i], None)
            i = 0
        return res

