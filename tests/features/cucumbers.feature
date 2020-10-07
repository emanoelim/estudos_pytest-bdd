Feature: Cucumber Basket
    As a gardener,
    I want to carry cucumbers in a basket,
    So that I don't drop them all.

   Scenario Outline: Add cucumbers to a basket
    Given the basket has <start> cucumbers
    When <add> cucumbers are added to the basket
    Then the basket contains <total> cucumbers

    Examples: Vertical
    | start  | 12 | 2 | 30  |
    | add    | 5  | 1 | 90  |
    | total  | 17 | 3 | 100 |

   Scenario Outline: Add to many cucumbers to a basket
    Given the basket has <start> cucumbers
    When <add> cucumbers are added to the basket
    Then the basket contains <total> cucumbers

    Examples:
    | start | add | total |
    | 30    | 80  | 100   |
    | 40    | 70  | 100   |

   Scenario Outline: Remove cucumbers to a basket
    Given the basket has <start> cucumbers
    When <remove> cucumbers are removed to the basket
    Then the basket contains <total> cucumbers

    Examples: Vertical
    | start  | 12 | 2 | 10 |
    | remove | 5  | 1 | 11 |
    | total  | 7  | 1 | 0  |