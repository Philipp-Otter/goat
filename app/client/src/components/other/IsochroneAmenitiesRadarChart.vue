<script>
import { Radar } from "vue-chartjs";
import { mapGetters } from "vuex";
import { EventBus } from "../../EventBus";

export default {
  extends: Radar,
  mounted() {
    this.renderRadarChart();
    EventBus.$on("ol-interaction-activated", interaction => {
      if (interaction === "languageChange") {
        this.renderRadarChart();
      }
    });
  },
  methods: {
    renderRadarChart: function() {
      let labels;
      if (this.chartDatasetType === 1) {
        labels = this.selectedPoisOnlyKeys.map(key => this.translatePOI(key));
      } else if (this.chartDatasetType === 2) {
        labels = this.selectedAoisOnlyKeys.map(key => this.translatePOI(key));
      }
      if (this.chartDatasetType === 2) {
        labels = this.selectedAoisOnlyKeys;
      }
      const datasets = [];

      this.selectedCalculations.forEach(calculation => {
        const calculationData = calculation.surfaceData.accessibility;
        // add only amenities
        const data = [];
        let keys = [];
        if (this.chartDatasetType === 1) {
          keys = this.selectedPoisOnlyKeys;
        } else if (this.chartDatasetType === 2) {
          keys = this.selectedAoisOnlyKeys;
        }
        keys.forEach(amenity => {
          if (calculationData[amenity]) {
            data.push(calculationData[amenity][this.isochroneRange - 1]);
          }
        });
        datasets.push({
          data,
          label: `Isochrone - ${calculation.id}`,
          backgroundColor:
            this.preDefCalculationColors[calculation.id - 1] ||
            "rgb(54, 162, 235)"
        });
      });

      this.renderChart(
        {
          labels,
          datasets
        },
        {
          responsive: true,
          maintainAspectRatio: false,
          animation: {
            duration: 0
          }
        }
      );
    },
    translatePOI: function(key) {
      const canTranslate = this.$te(`pois.${key}`);
      if (canTranslate) {
        return this.$t(`pois.${key}`);
      } else {
        return key;
      }
    }
  },
  watch: {
    selectedPoisOnlyKeys: {
      handler: function() {
        this.renderRadarChart();
      },
      deep: true
    },
    selectedAoisOnlyKeys: {
      handler: function() {
        this.renderRadarChart();
      },
      deep: true
    },
    isochroneRange: function() {
      this.renderRadarChart();
    },
    chartDatasetType: function() {
      this.renderRadarChart();
    },
    selectedCalculations() {
      this.renderRadarChart();
    }
  },
  computed: {
    ...mapGetters("isochrones", {
      selectedCalculations: "selectedCalculations",
      isochroneRange: "isochroneRange",
      chartDatasetType: "chartDatasetType",
      preDefCalculationColors: "preDefCalculationColors"
    }),
    ...mapGetters("poisaois", {
      selectedPoisOnlyKeys: "selectedPoisOnlyKeys",
      selectedAoisOnlyKeys: "selectedAoisOnlyKeys"
    }),
    ...mapGetters("app", {
      poisConfig: "poisConfig",
      aoisConfig: "aoisConfig"
    })
  }
};
</script>
