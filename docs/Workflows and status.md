# Workflows and Statuses

## Purpose

This document defines how GRC records move through creation, review, approval, remediation, and closure.

## General Record Workflow

Draft → Submitted for Review → Approved / Rejected → Under Review → Closed / Archived

## Risk Workflow

Draft → Assessed → Treatment Planned → Submitted for Approval → Approved → Under Treatment → Residual Risk Reviewed → Accepted / Reopened → Closed

## Control Workflow

Draft → Planned → In Progress → Implemented → Under Review → Effective / Needs Improvement

## Statement of Applicability Workflow

Draft → Submitted for Review → Approved / Rejected → Change Requested → Reapproved

## Evidence Workflow

Draft → Submitted → Under Review → Accepted / Rejected → Expired

## Incident Workflow

Reported → Triage → Contained → Investigating → Recovering → Monitoring → Closed

## Approval Rules

- A record creator must not approve their own submission.
- Rejection must include a comment.
- Change requests must identify what needs correction.
- Approved records must record the approver, date, and decision.
- Important status changes must create an audit-history entry.
- Closed records should be archived rather than permanently deleted where historical evidence is required.

## Required Status Information

Each workflow record should store:

- Current status
- Assigned owner
- Previous status
- Status-change date
- Person who changed the status
- Comment or reason
- Next action
- Due date, where applicable

