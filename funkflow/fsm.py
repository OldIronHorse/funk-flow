#!/usr/bin/env python3

from enum import Enum
from collections import namedtuple

State = Enum('State', 'S0 S1 S2 S3 S4')
Event = Enum('Event', 'E1 E2 E3 E4 E5 E6 E7')

transitions = {
  State.S0: {
    Event.E1: State.S1,
    Event.E2: State.S2},
  State.S1: {
    Event.E4: State.S3},
  State.S2: {
    Event.E3: State.S2,
    Event.E7: State.S4},
  State.S3: {
    Event.E5: State.S1,
    Event.E6: State.S4}}

WorkItem = namedtuple('WorkItem', 'state history')

def new():
  return WorkItem(state=State.S0, history=[])

def apply_event(event, workitem):
  new_state = transitions[workitem.state][event]
  return WorkItem(new_state, workitem.history + [(workitem.state, event)])

def is_terminal(state):
  return state == State.S4
