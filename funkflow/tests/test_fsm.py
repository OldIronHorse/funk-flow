#!/usr/bin/env python3

from unittest import TestCase
from funkflow import new, State, apply_event, Event, WorkItem

class TestFSM(TestCase):
  def test_new(self):
    self.assertEqual(WorkItem(State.S0, []), new())

  def test_valid_transition(self):
    self.assertEqual(WorkItem(state=State.S1, history=[(State.S0, Event.E1)]), 
                     apply_event(Event.E1, new()))

  def test_invalid_transition(self):
    with self.assertRaises(KeyError):
      apply_event(Event.E7, WorkItem(State.S0,[]))
