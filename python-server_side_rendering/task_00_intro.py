#!/usr/bin/python3
""" function to replace words in templates """

import logging
import os


def generate_invitations(template, attendees):
    """ function to replace templates with a list of dicts"""
    # Input checking - types
    if not isinstance(template, str):
        logging.error("Tamplate should be a string")
        raise ValueError("Not a string")

    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        logging.error("Attendees should be a list of dictionaries")
        raise ValueError("Not a list")

    # check empty inputs
    if not template:
        logging.error("Tamplate is empty, no output files generated.")
        raise IndexError("Tamplate is empty, no output files generated.")

    if not attendees:
        logging.error("No data provided, no output files generated.")
        raise IndexError("No data provided, no output files generated.")


    # Start index from 1
    for index, attendee in enumerate(attendees, start=1):
        output_content = template
        for key, value in attendee.items():
            if value is None:
                attendee[key] = "N/A"
            output_content = output_content.replace(f"{{{key}}}", attendee[key])

        # Output file
        # name = attendee.get("name", f"attendee_{index}").replace(" ", "_")
        output_filename = f"output_{index}.txt"

        # check if file already exists
        if os.path.exists(output_filename):
            logging.warning("File %s already exists, skipping.", output_filename)
            continue

        try:
            with open(output_filename, "w", encoding="utf-8") as output_file:
                output_file.write(output_content)
            logging.info("Generated file: %s", output_filename)
        except Exception as e:
            logging.exception("Failed to write to file %s: %s", output_filename, e)

    logging.info("Invitation files generated successfully.")
