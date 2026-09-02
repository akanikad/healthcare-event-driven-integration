# Topic Strategy

## Topic naming

`<bounded-context>.<aggregate>.<event>`

Examples:
- `prior-auth.authorization.requested`
- `prior-auth.authorization.review-required`
- `claims.claim.status-updated`

## Partitioning

Partition by aggregate identifier when ordering is required for that aggregate.

## Retention

Retention should reflect replay requirements, regulatory constraints, downstream recovery needs, and cost.

## DLQ

DLQ records should preserve the original event metadata, failure reason, attempt count, and correlation identifiers without copying unnecessary sensitive data.
