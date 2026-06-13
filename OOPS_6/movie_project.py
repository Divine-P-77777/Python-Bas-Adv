class Movie:
    def __init__(self, movie_name, total_seats, ticket_price):
        self.movie_name = movie_name
        self.total_seats = total_seats
        self.ticket_price = ticket_price
        self.booked_seats = 0

    def book_ticket(self, num_tickets):
        available_seats = self.total_seats - self.booked_seats

        if num_tickets <= available_seats:
            self.booked_seats += num_tickets
            total_amount = num_tickets * self.ticket_price

            print("Booking Successful!")
            print("Tickets Booked:", num_tickets)
            print("Total Amount to Pay:", total_amount)
        else:
            print("Sorry, not enough seats available")

    def show_status(self):
        available_seats = self.total_seats - self.booked_seats

        print("\nMovie Name:", self.movie_name)
        print("Seats Available:", available_seats)
        print("Seats Booked:", self.booked_seats)


# Example Usage
movie1 = Movie("Avengers", 100, 250)

movie1.show_status()

movie1.book_ticket(5)

movie1.show_status()

movie1.book_ticket(120)