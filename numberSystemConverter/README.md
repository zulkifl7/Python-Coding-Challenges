In this coding challenge i'm crating a solution to convert between different number systems!


Build History
-------------
13/04/2024 - 3:14 PM
At this moment we have 2 Functions

1 - decimal_to(dec,system)   :   (num: Any, system: Any) -> None 
    * which convert decimal to other number systems
    * Takes 2 arguments adn return nothing
            1 - decimal number which we want to convert to another number system
            2 - In which number system we want it to converted 
                    2 - Binry
                    8 - Octal
                    16 - Hexa decimal

2 - to_decimal(num, system)   :     (num: Any, system: Any) -> None
    * which convert any number to decimal
    * Takes 2 arguments and return nothing
            1 - the number we want to convert to decimal
            2 -  in which number system it is at the moment
                    2 - Binry
                    8 - Octal
                    16 - Hexa decimal


3 - octal_hex_to_binary(unm, num_system)     :     (num: Any, num_system: Any) -> None                    
    * Which convert hexadecimal and octal numbers into binary number
	* Takes 2 arguments and return nothing
			1 - the number we want to convert to binary
			2 -  the number system in which it is already
					8 - Octal
					16 - Hexa decimal
