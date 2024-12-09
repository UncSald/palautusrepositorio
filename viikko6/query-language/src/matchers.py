class And:
    def __init__(self, *matchers):
        self._matchers = matchers
    def test(self, player):
        for matcher in self._matchers:
            if not matcher.test(player):
                return False
        return True


class PlaysIn:
    def __init__(self, team):
        self._team = team

    def test(self, player):
        return player.team == self._team


class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value

class All:
    def __init__(self):
        pass

    def test(self, player):
        return True

class Not:
    def __init__(self, test_to_negate):
        self._test_to_negate = test_to_negate

    def test(self, player):
        result = self._test_to_negate.test(player)

        return not result


class HasFewerThan:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)
        return player_value < self._value

class Or:
    def __init__(self, *matchers):
        self._matchers = matchers
        
    def test(self, player):
        for match in self._matchers:
            if match.test(player):
                return True
        return False

class QueryBuilder:
    def __init__(self, matcher = All(), stack = []):
        self._stack = stack
        self._stack.append(matcher)

    def build(self):
        all_items = And(*self._stack)
        return all_items
    
    def plays_in(self, team):
        new_query = QueryBuilder(PlaysIn(team), self._stack)
        self._stack = []
        return new_query
    
    def has_at_least(self,value,attr):
        new_query = QueryBuilder(HasAtLeast(value,attr), self._stack)
        self._stack = []
        return new_query
    
    def has_fewer_than(self, value, attr):
        new_query = QueryBuilder(HasFewerThan(value,attr), self._stack)
        self._stack = []
        return new_query

    def one_of(self, query_one, query_two):
        new_query = QueryBuilder(Or(query_one, query_two), self._stack)
        return new_query
