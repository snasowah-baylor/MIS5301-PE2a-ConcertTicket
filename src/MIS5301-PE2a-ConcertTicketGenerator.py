# -----------------------------------------------------------
# Name: Sowah, Stephen
# Course: MIS 5301
# Purpose: Concert Ticket Generator (No User Input)
# File: MIS5301-PE2a-ConcertTicketGenerator.py
# -----------------------------------------------------------

TAX_RATE = 0.0825


def calculate_ticket_total(section_price, num_tickets):
    """Return total price before tax."""
    return section_price * num_tickets


def calculate_tax(total_ticket_price, tax_rate=TAX_RATE):
    """Return sales tax amount."""
    return total_ticket_price * tax_rate


def calculate_total_with_tax(total_ticket_price, sales_tax):
    """Return total price including tax."""
    return total_ticket_price + sales_tax


def main():
    # -- Test Data --------------------------------------------------
    artist_name = "Baylor Symphony"
    concert_date = "October 11, 2025"
    concert_time = "7pm"
    venue = "Foster Pavilion"
    seat_section = "Gold"
    section_price = 40.25
    num_tickets = 4

    # -- Input ------------------------------------------------------
    # TODO: Replace hardcoded test data with input() calls in a later chapter

    # -- Process ----------------------------------------------------
    total_ticket_price = calculate_ticket_total(section_price, num_tickets)
    sales_tax = calculate_tax(total_ticket_price)
    total_with_tax = calculate_total_with_tax(total_ticket_price, sales_tax)

    # -- Output -----------------------------------------------------
    print()
    print(" *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print()
    print(f"                      {artist_name}")
    print()
    print("          Date              Time            Venue")
    print("        ---------         ---------        --------")
    print(f"    {concert_date}         {concert_time}        {venue}")
    print()
    print()
    print(f"                           Section: {seat_section}")
    print(f"                 Number of Tickets: {num_tickets}")
    print(
        f"            Total Ticket Price ($): {total_ticket_price}"
    )  # fix format later
    print(f"                    Tax Amount ($): {sales_tax}")  # fix format later
    print(f"                Total with Tax ($): {total_with_tax}")  # fix format later
    print()
    print("                       Enjoy the Show!")
    print()
    print(" *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print()


if __name__ == "__main__":
    main()
