CC = gcc
CFLAGS = -Wall -Wextra -O2

TARGET = mmse_wiener

SRC = main.c wiener_filter.c

all: $(TARGET)

$(TARGET): $(SRC)
	$(CC) $(CFLAGS) -o $(TARGET) $(SRC) -lm

run: $(TARGET)
	./$(TARGET)

clean:
	rm -f $(TARGET)