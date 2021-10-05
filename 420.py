class Solution:
    def step(self, password: str):
        result = list(password)

        n_chars = len(password)
        n_chars_to_add = 0

        if n_chars < 6:
            n_chars_to_add = 6 - n_chars
        elif n_chars > 20:
            n_chars_to_add = 20 - n_chars


        digits = 0
        lowers = 0
        uppers = 0
        repeats = False
        repeater_to_remove = None
        repeater_reps = None

        # Special chars:
        # digit: #
        # lower: $
        # upper: %
        special_chars = ["#", "$", "%"]

        i = 0
        while i < n_chars:
            c = password[i]

            if c.isdigit() or c == "#":
                digits += 1
            elif c.islower() or (c == "$"):
                lowers += 1
            elif c.isupper() or (c == "%"):
                uppers += 1

            # Other character
            if i < n_chars - 2 and c not in special_chars and c == password[i + 1] == password[i + 2]:
                # TODO: Find optimum chars to change.
                repeats = True

                reps = 3

                # Might not be necessary.
                for c2 in password[i + 3:]:
                    if c2 != c:
                        break

                    reps += 1

                if repeater_to_remove is None or reps % 3 == 0 or (
                    repeater_reps % 3 > reps % 3
                ):
                    repeater_to_remove = i + 2
                    repeater_reps = reps

                i += reps

                continue

            i += 1

        if repeats:
            c_to_add = "$"

            if not digits:
                c_to_add = "#"
            if not lowers:
                c_to_add = "$"
            elif not uppers:
                c_to_add = "%"

            if n_chars_to_add > 0:
                result.insert(repeater_to_remove, c_to_add)
            elif n_chars_to_add < 0:
                result.pop(repeater_to_remove)
            else:
                result[repeater_to_remove] = c_to_add
        # Add
        elif n_chars_to_add > 0:
            char_to_add = "#"

            if not digits:
                char_to_add = "#"
            elif not lowers:
                char_to_add = "$"
            elif not uppers:
                char_to_add = "%"

            result.append(char_to_add)
        # Remove
        elif n_chars_to_add < 0:
            if digits > 1 or lowers > 1 or uppers > 1:
                for i, c in enumerate(password):
                    if (
                        (digits > 1 and (c.isdigit() or c == "#")) or
                        (lowers > 1 and (c.islower() or c == "$")) or
                        (uppers > 1 and (c.isupper() or c == "%"))
                    ):
                        # NOTE: Pop may cause repetition. Might have to check.
                        # Pop should always remove the first one so might never cause rep.
                        result.pop(i)

                        break
                else:
                    raise Exception()
            # No important characters. Then there has to be junk characters (., !).
            else:
                for i, c in enumerate(password):
                    if c == "!" or c == ".":
                        # NOTE: Pop may cause repetition.
                        result.pop(i)

                        break
                else:
                    raise Exception()
        # Replace
        elif not digits or not lowers or not uppers:
            char_to_add = "#"

            if not digits:
                char_to_add = "#"
            elif not lowers:
                char_to_add = "$"
            elif not uppers:
                char_to_add = "%"

            if digits > 1 or lowers > 1 or uppers > 1:
                for i, c in enumerate(password):

                    if (
                        (digits > 1 and (c.isdigit() or c == "#")) or
                        (lowers > 1 and (c.islower() or c == "$")) or
                        (uppers > 1 and (c.isupper() or c == "%"))
                    ):
                        result[i] = char_to_add

                        break
                else:
                    raise Exception()
            # No important characters. Then there has to be junk characters (., !).
            else:
                for i, c in enumerate(password):
                    if c == "!" or c == ".":
                        result[i] = char_to_add

                        break
                else:
                    raise Exception()

        return "".join(result)


    def strongPasswordChecker(self, password: str) -> int:
        for i in range(50):
            new_password = self.step(password)

            if new_password == password:
                return i

            password = new_password

        raise Exception()

if __name__ == "__main__":
    print(Solution().strongPasswordChecker("a") == 5)
    print(Solution().strongPasswordChecker("aA1") == 3)
    print(Solution().strongPasswordChecker("1337C0d3") == 0)
    print(Solution().strongPasswordChecker("!!!!aB!!!!") == 2)
    print(Solution().strongPasswordChecker("aaa111") == 2)
    print(Solution().strongPasswordChecker("bbaaaaaaaaaaaaaaacccccc") == 8)
    print(Solution().strongPasswordChecker("aaaaabbbb1234567890ABA") == 3)
