# -----------------------------------------------------------
# Name: Sowah, Stephen
# Course: MIS 5301
# Purpose: Concert Ticket Generator (No User Input)
# File: MIS5301-PE2a-ConcertTicketGenerator.py
# -----------------------------------------------------------

# -- Test Data ------------------------------------------------------
artist_name = "Baylor Symphony"
concert_date = "October 11, 2025"
concert_time = "7pm"
venue = "Foster Pavilion"
seat_section = "Gold"
section_price = 40.25
num_tickets = 4

# -- Input ----------------------------------------------------------
# TODO: Replace hardcoded test data with input() calls in a later chapter

# -- Process --------------------------------------------------------
total_ticket_price = section_price * num_tickets
tax_amount = total_ticket_price * 0.0825
total_with_tax = total_ticket_price + tax_amount
