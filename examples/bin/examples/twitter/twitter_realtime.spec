{
  "description": "Ingestion spec for Twitter spritzer. Dimension values taken from io.druid.examples.twitter.TwitterSpritzerFirehoseFactory",
  "spec": {
    "dataSchema": {
      "dataSource": "twitterstream",
      "granularitySpec": {
        "queryGranularity": "all",
        "segmentGranularity": "hour",
        "type": "uniform"
      },
      "metricsSpec": [
        {
          "name": "tweets",
          "type": "count"
        },
        {
          "fieldName": "follower_count",
          "name": "total_follower_count",
          "type": "doubleSum"
        },
        {
          "fieldName": "retweet_count",
          "name": "total_retweet_count",
          "type": "doubleSum"
        },
        {
          "fieldName": "friends_count",
          "name": "total_friends_count",
          "type": "doubleSum"
        },
        {
          "fieldName": "statuses_count",
          "name": "total_statuses_count",
          "type": "doubleSum"
        },
        {
          "fieldName": "text",
          "name": "text_hll",
          "type": "hyperUnique"
        },
        {
          "fieldName": "user_id",
          "name": "user_id_hll",
          "type": "hyperUnique"
        },
        {
          "fieldName": "contributors",
          "name": "contributors_hll",
          "type": "hyperUnique"
        },
        {
          "fieldName": "htags",
          "name": "htags_hll",
          "type": "hyperUnique"
        },
        {
          "fieldName": "follower_count",
          "name": "min_follower_count",
          "type": "min"
        },
        {
          "fieldName": "follower_count",
          "name": "max_follower_count",
          "type": "max"
        },
        {
          "fieldName": "friends_count",
          "name": "min_friends_count",
          "type": "min"
        },
        {
          "fieldName": "friends_count",
          "name": "max_friends_count",
          "type": "max"
        },
        {
          "fieldName": "statuses_count",
          "name": "min_statuses_count",
          "type": "min"
        },
        {
          "fieldName": "statuses_count",
          "name": "max_statuses_count",
          "type": "max"
        },
        {
          "fieldName": "retweet_count",
          "name": "min_retweet_count",
          "type": "min"
        },
        {
          "fieldName": "retweet_count",
          "name": "max_retweet_count",
          "type": "max"
        }
      ],
      "parser": {
        "parseSpec": {
          "dimensionsSpec": {
            "dimensions": [
              "text",
              "htags",
              "contributors",
              "lat",
              "lon",
              "retweet_count",
              "follower_count",
              "friendscount",
              "lang",
              "utc_offset",
              "statuses_count",
              "user_id",
              "ts"
            ],
            "dimensionExclusions": [
            ],
            "spatialDimensions": [
              {
                "dimName": "geo",
                "dims": [
                  "lat",
                  "lon"
                ]
              }
            ]
          },
          "format": "json",
          "timestampSpec": {
            "column": "ts",
            "format": "millis"
          }
        }
      }
    },
    "ioConfig": {
      "firehose": {
        "maxEventCount": 500000,
        "maxRunMinutes": 120,
        "type": "twitzer"
      },
      "type": "realtime"
    },
    "tuningConfig": {
      "intermediatePersistPeriod": "PT10m",
      "maxRowsInMemory": 500000,
      "type": "realtime",
      "windowPeriod": "PT10m"
    }
  },
  "type": "index_realtime"
}