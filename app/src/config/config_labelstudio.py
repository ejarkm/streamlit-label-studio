# Label Studio

LABEL_CONFIG = """
    <View>
      <RectangleLabels name="label" toName="image" opacity="1" fillColor="#ff0000">
        <Label value="Band"></Label>
      </RectangleLabels>
      <Image name="image" value="$image" brightnessControl="true" contrastControl="true" zoomControl="true" rotateControl="true"/>
    </View>
    """

LABEL_INTERFACES = (
    [
        "panel",
        "update",
        "controls",
        "side-column",
        "completions:menu",
        "completions:add-new",
        "completions:delete",
        "predictions:menu",
    ],
)

LABEL_USER = ({"pk": 1, "firstName": "Western", "lastName": "Blot"},)
