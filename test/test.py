import typing
import unittest
from isinstancex.parser import *


class ParserTestCase(unittest.TestCase):
    def test_is_hint(self):
        hints = (typing.Any,
                 typing.Union[str, int, float],
                 typing.Union[typing.Union[str, int], float],
                 str | int | float,
                 typing.Tuple[str, int, float],
                 typing.Tuple[typing.Tuple[str, int], float],
                 tuple[str, int, float],
                 tuple[tuple[str, int], float],
                 typing.List[str],
                 typing.List[typing.Union[str, int]],
                 list[str],
                 list[str | int],
                 typing.Dict[str, int],
                 typing.Dict[typing.Union[str, int], typing.Tuple[float, int]],
                 dict[str, int],
                 dict[str | int, tuple[float, int]],
                 typing.Set[str],
                 typing.Set[typing.Union[str, int]],
                 set[str],
                 set[str | int])
        self.assertTrue(all([TypeHintChecker(hint).is_hint for hint in hints]))

    def test_is_any(self):
        hint = typing.Any
        self.assertTrue(TypeHintChecker(hint).is_any)

    def test_is_union(self):
        hints = (typing.Union[str, int, float],
                 typing.Union[typing.Union[str, int], float],
                 str | int | float)
        self.assertTrue(all([TypeHintChecker(hint).is_union for hint in hints]))

    def test_is_tuple(self):
        hints = (typing.Tuple[str, int, float],
                 typing.Tuple[typing.Tuple[str, int], float],
                 tuple[str, int, float],
                 tuple[tuple[str, int], float])
        self.assertTrue(all([TypeHintChecker(hint).is_tuple for hint in hints]))

    def test_is_list(self):
        hints = (typing.List[str],
                 typing.List[typing.Union[str, int]],
                 list[str],
                 list[str | int])
        self.assertTrue(all([TypeHintChecker(hint).is_list for hint in hints]))

    def test_is_dict(self):
        hints = (typing.Dict[str, int],
                 typing.Dict[typing.Union[str, int], typing.Tuple[float, int]],
                 dict[str, int],
                 dict[str | int, tuple[float, int]])
        self.assertTrue(all([TypeHintChecker(hint).is_dict for hint in hints]))

    def test_is_set(self):
        hints = (typing.Set[str],
                 typing.Set[typing.Union[str, int]],
                 set[str],
                 set[str | int])
        self.assertTrue(all([TypeHintChecker(hint).is_set for hint in hints]))

    def test_parse(self):
        args = ((typing.Tuple, (1, 2)),
                (typing.Tuple[int, str], (1, "1")),
                (typing.List[int | str], [1, "2", "3", 4]),
                (typing.Dict[str, int | str], {"1": 1, "2": "2"}),
                (typing.Optional[int], 1))
        self.assertTrue(all([parse(*i) for i in args]))


if __name__ == "__main__":
    unittest.main()
