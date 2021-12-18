# This entrypoint file to be used in development. Start by reading README.md
from time_calculator import add_time
from unittest import main


add_time("11:06 PM", "2:02")
add_time("3:30 PM", "2:12") 
# expected = "5:42 PM"
add_time("11:55 AM", "3:12")         
# expected = "3:07 PM"
add_time("9:15 PM", "5:30")      
# expected = "2:45 AM (next day)"
add_time("11:40 AM", "0:25")     
# expected = "12:05 PM"
add_time("2:59 AM", "24:00")     
# expected = "2:59 AM (next day)"
add_time("11:59 PM", "24:05")    
# expected = "12:04 AM (2 days later)"
add_time("8:16 PM", "466:02")
# expected = "6:18 AM (20 days later)"
add_time("5:01 AM", "0:00")
# expected = "5:01 AM"
add_time("3:30 PM", "2:12", "Monday")
# expected = "5:42 PM, Monday"
add_time("2:59 AM", "24:00", "saturDay")
# expected = "2:59 AM, Sunday (next day)"
add_time("11:59 PM", "24:05", "Wednesday")
# expected = "12:04 AM, Friday (2 days later)"
add_time("8:16 PM", "466:02", "tuesday")
# expected = "6:18 AM, Monday (20 days later)"

# Run unit tests automatically
main(module='test_module', exit=False)