#!/usr/bin/env python3
# Developer: Hamdy Abou El Anein
# Contact: info@daylightlinux.ch
# SPDX-License-Identifier: GPL-3.0-only
"""Calculate the number of calendar days lived."""
from __future__ import annotations
import argparse
from datetime import date
import tkinter as tk
from tkinter import messagebox, ttk

def days_lived(birthday: date, today: date | None = None) -> int:
    today = today or date.today()
    if birthday > today:
        raise ValueError("Birth date cannot be in the future")
    return (today - birthday).days

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--name", help="Name for the greeting")
    parser.add_argument("--birthdate", help="Birth date in ISO format YYYY-MM-DD; CLI mode")
    args = parser.parse_args()
    if args.birthdate is not None:
        try:
            count = days_lived(date.fromisoformat(args.birthdate))
        except ValueError as exc:
            parser.error(str(exc))
        print(f"{args.name or 'You'}: {count} days lived")
        return
    root = tk.Tk()
    root.title("How Many Days Have You Lived?")
    root.geometry("430x255")
    frame = ttk.Frame(root, padding=20)
    frame.pack(fill="both", expand=True)
    name = tk.StringVar(value=args.name or "")
    birthday = tk.StringVar(value="2000-01-01")
    result = tk.StringVar()
    for row, (label, variable) in enumerate((("Name", name), ("Birth date (YYYY-MM-DD)", birthday))):
        ttk.Label(frame, text=label).grid(row=row, column=0, sticky="w", pady=8)
        ttk.Entry(frame, textvariable=variable, width=25).grid(row=row, column=1, pady=8)
    def calculate() -> None:
        try:
            count = days_lived(date.fromisoformat(birthday.get()))
        except ValueError as exc:
            messagebox.showerror("Invalid date", str(exc), parent=root)
            return
        result.set(f"{name.get().strip() or 'You'}: {count:,} days lived")
    ttk.Button(frame, text="Calculate", command=calculate).grid(row=2, column=0, columnspan=2, pady=12)
    ttk.Label(frame, textvariable=result).grid(row=3, column=0, columnspan=2)
    root.mainloop()

if __name__ == "__main__":
    main()
