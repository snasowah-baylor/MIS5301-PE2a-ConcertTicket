# -----------------------------------------------------------
# Tests for MIS5301-PE2a-ConcertTicketGenerator
# -----------------------------------------------------------

import importlib.util
import os

# Load module despite hyphenated filename
_src = os.path.join(
    os.path.dirname(__file__),
    "..",
    "src",
    "MIS5301-PE2a-ConcertTicketGenerator.py",
)
_spec = importlib.util.spec_from_file_location("concert_ticket", _src)
concert_ticket = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(concert_ticket)


class TestCalculateTicketTotal:
    def test_basic_multiplication(self):
        assert concert_ticket.calculate_ticket_total(40.25, 4) == 161.0

    def test_single_ticket(self):
        assert concert_ticket.calculate_ticket_total(50.00, 1) == 50.00

    def test_zero_tickets(self):
        assert concert_ticket.calculate_ticket_total(40.25, 0) == 0.0


class TestCalculateTax:
    def test_default_tax_rate(self):
        result = concert_ticket.calculate_tax(161.0)
        assert abs(result - 13.2825) < 1e-9

    def test_custom_tax_rate(self):
        result = concert_ticket.calculate_tax(100.0, tax_rate=0.10)
        assert abs(result - 10.0) < 1e-9

    def test_zero_total(self):
        assert concert_ticket.calculate_tax(0.0) == 0.0


class TestCalculateTotalWithTax:
    def test_adds_correctly(self):
        result = concert_ticket.calculate_total_with_tax(161.0, 13.2825)
        assert abs(result - 174.2825) < 1e-9

    def test_zero_tax(self):
        assert concert_ticket.calculate_total_with_tax(100.0, 0.0) == 100.0
