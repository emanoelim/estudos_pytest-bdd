Feature: Cucumber Basket
    As a gardener,
    I want to carry cucumbers in a basket,
    So that I don't drop them all.

   Scenario Outline: Add cucumbers to a basket
    Given the basket has <start> cucumbers
    When <add> cucumbers are added to the basket
    Then the basket contains <total> cucumbers

    Examples: Vertical
    | start  | 12  | 2 |
    | add    | 5   | 1 |
    | total  | 17  | 3 |


   Scenario Outline: Add to many cucumbers to a basket
    Given the basket has <start> cucumbers
    When <add> cucumbers are added to the basket
    Then the basket contains <total> cucumbers

    Examples:
    | start | add | total |
    | 30 | 80 | 100 |
    | 40 | 70 | 100 |
