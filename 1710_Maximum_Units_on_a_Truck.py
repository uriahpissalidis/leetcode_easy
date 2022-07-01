class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda k: (k[1]), reverse=True)
        boxes, units = 0, 0 
        for boxes, b_units in boxTypes:
            if boxes <= truckSize:
                truckSize = truckSize - boxes
                units += boxes*b_units
            else:
                units += truckSize*b_units
                break
        return units