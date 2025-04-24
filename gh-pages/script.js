// Palettes intégrées directement dans le code
const allPalettes = {
    3: [
        ["#c4500c", "#9a966d", "#411089"],
        ["#65d571", "#571e5e", "#0d7f25"],
        ["#3fdd8b", "#eb3b7d", "#1441ef"],
        ["#726537", "#92a80c", "#a5d2a2"],
        ["#f685e6", "#776b6f", "#9f260b"],
        ["#964387", "#8fa04b", "#9ce31c"],
        ["#daafc4", "#1555c6", "#6d1486"],
        ["#16210b", "#b1b7d9", "#947d77"],
        ["#cfd8bc", "#415b95", "#4216f4"],
        ["#b88f3f", "#833eb4", "#0516cc"],
        ["#ea29ee", "#72d881", "#f3f84f"],
        ["#bba83f", "#6c4a28", "#a7788d"],
        ["#065e19", "#9ce6a6", "#1d8b35"],
        ["#0a1dbe", "#965bdb", "#c6d458"],
        ["#745b2c", "#a572a9", "#5a0c6e"],
        ["#3bb672", "#114b85", "#fba6e3"],
        ["#0dc7f6", "#c30168", "#fed460"],
        ["#6be66d", "#576c7a", "#c9829c"],
        ["#62136f", "#a7cd39", "#4fad69"],
        ["#1b1a47", "#b8c8b7", "#9383b9"],
        ["#8e5800", "#b462bd", "#d18ecf"],
        ["#9805da", "#09a3d2", "#c3e1c5"],
        ["#510a28", "#533c51", "#9e53a6"],
        ["#0917e4", "#d8bbe6", "#5b9b35"],
        ["#189ef5", "#e7ae1c", "#f808d6"],
        ["#c6eb57", "#77413b", "#79ad68"],
        ["#208bf2", "#30e8ca", "#8520c5"],
        ["#d3d35c", "#2a8449", "#5e05fc"],
        ["#442ed9", "#54094e", "#6ea010"],
        ["#cc2cdf", "#98c640", "#8a706a"],
        ["#77d13c", "#5a8bbe", "#b0ecde"],
        ["#c4400c", "#969c22", "#c2f47d"],
        ["#0aa430", "#9cf80d", "#19032e"],
        ["#0f5ed8", "#3f976d", "#57f5e8"],
        ["#924e9f", "#d7902e", "#97e174"],
        ["#748979", "#63030b", "#79402b"],
        ["#4cae90", "#e453b6", "#8539ab"],
        ["#f267ef", "#ecc7d4", "#dc4528"],
        ["#0b8b0c", "#980006", "#0ab285"],
        ["#5bd8e7", "#64a4a8", "#503f6c"],
        ["#a53cd3", "#a3ea9e", "#b61853"],
        ["#3fbf1b", "#abbee8", "#952bc9"],
        ["#a504a3", "#22ad81", "#ed2dcd"],
        ["#410c84", "#b322e5", "#6e936e"],
        ["#58e944", "#872311", "#576406"],
        ["#a16f66", "#54c6eb", "#060f54"],
        ["#9361bb", "#2f18be", "#44ab6e"],
        ["#a0f888", "#53afe8", "#1d3e4a"],
        ["#d791e7", "#db6d75", "#9e1038"],
        ["#d737fe", "#48379d", "#97f895"],
        ["#10ea56", "#fb0755", "#a1551a"],
        ["#f697b8", "#fc713f", "#413dea"],
        ["#fddb8c", "#8a5678", "#7c9619"],
        ["#80667a", "#5caa30", "#d8d14f"],
        ["#2b2fc1", "#28fd85", "#eb4bb6"],
        ["#54df67", "#234598", "#df65d4"],
        ["#095528", "#4b778d", "#8ede69"],
        ["#a142e9", "#44fcee", "#f68ea8"],
        ["#ef86b8", "#990a2b", "#18a344"],
        ["#81cc6d", "#243673", "#0d6c5c"],
        ["#a9023f", "#6e6cfc", "#7adb12"],
        ["#3a645d", "#34ffa9", "#cf650d"],
        ["#9c9274", "#0fe9be", "#4f57ad"],
        ["#a0bb50", "#953381", "#91edff"],
        ["#9308e6", "#f8ecad", "#76a4ca"],
        ["#5aeec0", "#afa340", "#69867e"],
        ["#bab3e1", "#9b552d", "#5589d4"],
        ["#1409ca", "#7dbe1c", "#63803d"],
        ["#deaec2", "#993596", "#6c95d0"],
        ["#e25f69", "#2a449f", "#71d540"],
        ["#a1e2e5", "#e108ed", "#54be3b"],
        ["#c324c5", "#ced3a9", "#d2a313"],
        ["#1b7494", "#39f12a", "#ae282a"],
        ["#44d820", "#e9c9ea", "#5b4f53"],
        ["#86d60a", "#f5ffcc", "#54a83d"],
        ["#5d4962", "#d37568", "#93fd83"],
        ["#0f25dc", "#f9fe6d", "#f14552"],
        ["#3c9e32", "#ca2ed9", "#4dffa3"],
        ["#0ba7c7", "#8607d1", "#4ee941"],
        ["#9528ce", "#72649f", "#4fa904"],
        ["#5bb22d", "#6f328e", "#fac268"],
        ["#9c6468", "#7a3316", "#90c077"],
        ["#817ca6", "#97c3c0", "#d50a84"],
        ["#a45830", "#25bb72", "#5808f0"],
        ["#256b8a", "#4d2ce0", "#70cc12"],
        ["#4ea674", "#5d62c9", "#faaca2"],
        ["#8db1ef", "#bb5475", "#9a2306"],
        ["#9e3b23", "#52af06", "#13fb94"],
        ["#b10c27", "#5c6639", "#79aae5"],
        ["#c89c22", "#2f816b", "#0c512f"],
        ["#0e28d9", "#b2ff6e", "#ec4623"],
        ["#df1669", "#845bc1", "#3700d7"],
        ["#783875", "#f4b3c7", "#f262c0"],
        ["#2f7355", "#e6b65e", "#51306f"],
        ["#e434f9", "#57ad42", "#6416be"],
        ["#8be692", "#995fe8", "#2d04b8"],
        ["#5364ea", "#d6e7c1", "#0a615a"],
        ["#1221a2", "#67d0ff", "#4492e0"],
        ["#48522a", "#829f2a", "#160d95"],
        ["#da9e59", "#d85dc8", "#9121ad"]
    ],
    4: [
        ["#163763", "#26bd68", "#588040", "#f5ca4e"],
        ["#1287d1", "#bad638", "#72149e", "#fd1f7c"],
        ["#71d17e", "#5a61e4", "#daecbf", "#9a9735"],
        ["#1ab8ba", "#c33f3d", "#c6cc36", "#001108"],
        ["#164aeb", "#2e1f09", "#fd8cfc", "#7775f4"],
        ["#f9e6e5", "#c5b338", "#8301bd", "#a54400"],
        ["#4f878d", "#41c21c", "#b6d567", "#0d369c"],
        ["#4c9b09", "#721507", "#afc033", "#d41e95"],
        ["#5e7fc7", "#e8a672", "#e4f41b", "#080972"],
        ["#f6c7d7", "#f358e7", "#8d0619", "#8542f6"],
        ["#0289ea", "#a2be7a", "#efeee0", "#2b324d"],
        ["#3dbf3c", "#ebda86", "#746171", "#4d2d1e"],
        ["#ba9435", "#3fe2a7", "#ec4c89", "#c71070"],
        ["#0accc8", "#2a30e2", "#b1db98", "#ec4154"],
        ["#e6b41e", "#8867a3", "#7207d8", "#c9e7d2"],
        ["#8e9828", "#81fbb4", "#783bb8", "#cca2f5"],
        ["#7fa60b", "#d935d6", "#6e1c6a", "#a5ffca"],
        ["#1a74f1", "#6f0ca0", "#d8c556", "#2ab0a1"],
        ["#57fbaf", "#68313a", "#7fa397", "#dd32ca"],
        ["#5d8992", "#23de47", "#2a7005", "#def08e"],
        ["#43bcbc", "#d71515", "#8748ff", "#d2f192"],
        ["#b872dc", "#48dfa9", "#b42251", "#5a0762"],
        ["#7dea42", "#330741", "#61a374", "#6b3219"],
        ["#314299", "#f5a922", "#736925", "#1515b4"],
        ["#6921eb", "#ba6de5", "#9a4a74", "#15f29c"],
        ["#534896", "#739ef9", "#030ba0", "#818227"],
        ["#ce5c29", "#c3a2ec", "#632cde", "#231115"],
        ["#25d229", "#930970", "#a5f953", "#9360fc"],
        ["#acab2e", "#c334a9", "#85fce5", "#742144"],
        ["#3651c2", "#299efb", "#cdc3c0", "#301d92"],
        ["#acd53b", "#b36d15", "#b98fad", "#964352"],
        ["#970334", "#7ee70d", "#b431d6", "#26a77a"],
        ["#c04fa7", "#7d051f", "#08e7b3", "#3c36df"],
        ["#34be45", "#a94b67", "#ffe528", "#165015"],
        ["#e16edb", "#511dec", "#9a3d94", "#66ea6e"],
        ["#2e9ea9", "#f6b5e5", "#582f49", "#3275c5"],
        ["#f39d61", "#8b41fb", "#ba77c0", "#0e313d"],
        ["#7351a6", "#9ae1c0", "#857ab8", "#fd0c13"],
        ["#04bbfc", "#713e61", "#4c855f", "#cede38"],
        ["#9f0a60", "#72ba7a", "#80f29e", "#719547"],
        ["#a34cc5", "#272453", "#f06d05", "#12e8c3"],
        ["#ab2fb1", "#c5620d", "#c79578", "#0e2c03"],
        ["#b7563b", "#533853", "#719ddc", "#39fc07"],
        ["#bc4ad7", "#75c8f2", "#dc8a0a", "#5a0299"],
        ["#7dfc38", "#3030ed", "#d4811d", "#2d66ab"],
        ["#8e6560", "#b8ba11", "#1dabaa", "#0e301e"],
        ["#62332c", "#54baea", "#3470dd", "#619661"],
        ["#400e1a", "#c694bd", "#dfe5bb", "#77455e"],
        ["#d30327", "#76aa2d", "#55f120", "#39884f"],
        ["#6f42dd", "#fe7886", "#44fc63", "#de0736"],
        ["#4f167c", "#63d6ed", "#c659b2", "#cb3c3e"],
        ["#151ccd", "#94e95e", "#6b994f", "#b72fa1"],
        ["#3d5ff9", "#6abfb1", "#2d05ae", "#54344b"],
        ["#96b70e", "#3f22d7", "#06897e", "#8eeef1"],
        ["#dd8f1e", "#622035", "#c05cd4", "#cde26f"],
        ["#4733a6", "#9adaf1", "#21c508", "#93689d"],
        ["#22a9e0", "#2e24aa", "#7fdcfd", "#8942e0"],
        ["#49318e", "#4b889d", "#f4b689", "#1f0507"],
        ["#6c3abb", "#b16b04", "#77eee7", "#d4a50e"],
        ["#e421a0", "#51873d", "#e77dd2", "#faf1ea"],
        ["#72b578", "#defc5c", "#604499", "#4d0ce7"],
        ["#9a8093", "#cdac36", "#836d29", "#7c075f"],
        ["#f15e20", "#a5b1b1", "#c130b2", "#493422"],
        ["#50bf0b", "#d2d764", "#14943c", "#1340df"],
        ["#0d2666", "#d5c8d9", "#f25550", "#27bbd1"],
        ["#f32d35", "#a0bbc2", "#1201b1", "#672a0d"],
        ["#b47d79", "#e9d77b", "#481356", "#7c3c28"],
        ["#184d8d", "#91eaad", "#4a0a25", "#e235e1"],
        ["#5b2f99", "#937137", "#54ad9c", "#74f226"],
        ["#a98c5a", "#1e2e9e", "#a7ee5d", "#766c77"],
        ["#efa61a", "#035f42", "#8e828f", "#cbfe5b"],
        ["#cb0bad", "#18ab4b", "#70f660", "#1c743e"],
        ["#6c6696", "#da7076", "#2cdbc4", "#0e44e7"],
        ["#401b8b", "#7df61f", "#d04395", "#a7a822"],
        ["#423b83", "#052310", "#fb68ad", "#aed4af"],
        ["#9ca4a0", "#44efc6", "#9c5984", "#1219a8"],
        ["#49d679", "#0720e5", "#0753b4", "#a96eca"],
        ["#9ffb3c", "#25843c", "#7f0ba5", "#80add0"],
        ["#055989", "#c546cb", "#d7a292", "#928a67"],
        ["#89a7a3", "#9532d4", "#be0930", "#e154ce"],
        ["#882242", "#ce6edf", "#fc3185", "#52ddd1"],
        ["#36864b", "#2eca1f", "#d11a05", "#ddc8bb"],
        ["#f5ae13", "#b68229", "#fe0002", "#1c02bc"],
        ["#c63f8b", "#b7212a", "#e86ceb", "#9be813"],
        ["#4b0df9", "#ca4380", "#e0fc99", "#58f112"],
        ["#90930b", "#ce0f2e", "#d9faa3", "#f0ab3d"],
        ["#23b5a3", "#b335de", "#8be26c", "#172840"],
        ["#4a3d2b", "#0cee38", "#2ca967", "#395ece"],
        ["#4b31d5", "#e2af64", "#f26c15", "#fbfa4b"],
        ["#a21708", "#eaf5b9", "#a74b79", "#9b9604"],
        ["#19bbf1", "#04337e", "#7e8107", "#93e469"],
        ["#464a9c", "#b3fdd3", "#be68a8", "#041cd1"],
        ["#da81e8", "#bbe830", "#3b116f", "#ce6640"],
        ["#0d1d82", "#81ecf8", "#87394e", "#1eb747"],
        ["#44b6d0", "#f2d4b8", "#29702a", "#3f112b"],
        ["#226899", "#4f2499", "#0ef453", "#2a98cb"],
        ["#e3ee9c", "#e24349", "#591389", "#d3a010"],
        ["#cc4d4d", "#59fe0e", "#7ea23d", "#2f2020"],
        ["#2f7e6c", "#837bf3", "#6bec60", "#0a4749"],
        ["#12096f", "#33327e", "#69c475", "#0c8024"]
    ],
    5: [
        ["#84facc", "#c07d05", "#de87f7", "#825b95", "#872b2f"],
        ["#6c7188", "#6dc03c", "#1f2559", "#d9dc89", "#8e3cad"],
        ["#a7a869", "#514303", "#f23676", "#dfe3bc", "#ff52ee"],
        ["#e24787", "#d59c1c", "#a91c48", "#d7e90f", "#0e01e3"],
        ["#85bd20", "#3a7136", "#fcd3ac", "#58904b", "#7e1ddc"],
        ["#70288f", "#b4538a", "#76ffbd", "#e68705", "#190d53"],
        ["#2424f8", "#a3a9a3", "#877f17", "#dbfcc6", "#da2966"],
        ["#fb2d9c", "#dcb01e", "#94013b", "#bae3f5", "#7f8a29"],
        ["#4509d9", "#a73c45", "#8dd727", "#94856f", "#a4f7fb"],
        ["#69ae0e", "#f8a9ac", "#0f775e", "#463464", "#2d0201"],
        ["#498d15", "#ecda52", "#e41d1b", "#94a523", "#080084"],
        ["#9cedd6", "#d413ce", "#de9329", "#138271", "#560859"],
        ["#8285e4", "#104313", "#1c0809", "#86d35f", "#73694f"],
        ["#8e0b9e", "#e13c39", "#2ff1f1", "#29d003", "#040f34"],
        ["#d199b1", "#795cef", "#30391a", "#bdf056", "#0c075c"],
        ["#a1aa65", "#300820", "#a250c5", "#9d1680", "#cd6c9b"],
        ["#f2fb0e", "#b42dbc", "#20e43f", "#618428", "#3a0f8d"],
        ["#aca501", "#4fe493", "#7c4598", "#8e0e63", "#20042a"],
        ["#908121", "#68cb40", "#176fb2", "#3a1d47", "#50f9e1"],
        ["#7c7050", "#4be66d", "#1516d2", "#973036", "#24b2e1"],
        ["#e6063a", "#2ab3ad", "#76752d", "#e6bbb5", "#0402a8"],
        ["#48d54a", "#3e02ca", "#b2297b", "#709308", "#b7faa7"],
        ["#bfb056", "#c8d9b8", "#9e44fc", "#6a9120", "#ab0691"],
        ["#d759d5", "#bdc591", "#4d2c92", "#a05508", "#0f0740"],
        ["#a1b7c8", "#982f38", "#a5f6ce", "#5b8f41", "#50140c"],
        ["#23c281", "#f64fe1", "#3ef6d6", "#3e2a2e", "#8f4b01"],
        ["#c45d88", "#dfac36", "#261737", "#9827df", "#edda7c"],
        ["#75ac70", "#398004", "#db03e1", "#48fb1e", "#550097"],
        ["#3839ba", "#317f4d", "#27e4ed", "#729708", "#ecee9c"],
        ["#fe5ed4", "#ba4a20", "#c4eea1", "#56226b", "#d6a1b9"],
        ["#9be69b", "#a06232", "#4c3f13", "#0d186f", "#06bc8c"],
        ["#e34e6c", "#850778", "#5d3cdd", "#14d438", "#f0fdd4"],
        ["#558584", "#03d2bb", "#472ec0", "#320866", "#b24b30"],
        ["#0aa468", "#ffaca9", "#e83839", "#1616b7", "#dff0e5"],
        ["#22bbd7", "#f322ae", "#141397", "#488d54", "#efe430"],
        ["#5c11e9", "#9ea981", "#98fb66", "#d94059", "#2197d8"],
        ["#a2b978", "#be7672", "#1d346e", "#486c1a", "#a7e6df"],
        ["#2b8121", "#5128f0", "#c3cd34", "#bd6de1", "#e1f3d4"],
        ["#94e728", "#d531bf", "#5c1276", "#7aa3c1", "#667f7f"],
        ["#e6506a", "#22dd69", "#3803df", "#0a5945", "#8aefde"],
        ["#657264", "#de8e5d", "#9f2be8", "#83f6e3", "#200864"],
        ["#d56c38", "#0fea61", "#6606dc", "#2963ec", "#b6efcf"],
        ["#c0c39c", "#4d4daa", "#6b7f92", "#242819", "#39c318"],
        ["#584cb4", "#cf5ecd", "#dec87a", "#63b16a", "#9a0c3b"],
        ["#d37efd", "#351c47", "#57552f", "#e83fe3", "#c9fc8c"],
        ["#b301fe", "#39c47f", "#ea4f54", "#c2ea21", "#2f0513"],
        ["#8276e0", "#551aca", "#a8cc4d", "#7d4abf", "#ffe1d5"],
        ["#eb0303", "#c4e223", "#6250be", "#677cba", "#020c83"],
        ["#8bf467", "#3855b5", "#62bcce", "#2ba44f", "#3c3322"],
        ["#888285", "#d32420", "#2ee683", "#1c1a4d", "#ffebc3"],
        ["#9ddef2", "#b01297", "#209d03", "#41be6c", "#117641"],
        ["#ccd47f", "#b4565f", "#23af49", "#393443", "#0b0098"],
        ["#c738a6", "#9217db", "#ee5f5e", "#dbfa5a", "#c39afe"],
        ["#1b7914", "#ab67fe", "#5123e6", "#99aca7", "#c3d3eb"],
        ["#99238c", "#6aa4ba", "#dbe97b", "#5166d5", "#4c0c21"],
        ["#a0af55", "#0d0beb", "#f20377", "#e0dd8d", "#5c50fd"],
        ["#c100bf", "#d5335b", "#40ee67", "#28bd62", "#070649"],
        ["#1ba435", "#faebd6", "#87a0a8", "#2515de", "#6d4efa"],
        ["#9c50f6", "#18fbcf", "#8f913d", "#8e380c", "#431c34"],
        ["#7c905f", "#2a417a", "#5bf69e", "#86537a", "#2b0cb6"],
        ["#285e87", "#90a5e6", "#b8fbe0", "#6e6eb3", "#2724d9"],
        ["#537702", "#144681", "#60b615", "#72f216", "#6b0330"],
        ["#011f8f", "#b39804", "#cc5122", "#21ffef", "#523eb5"],
        ["#744463", "#988a73", "#262b90", "#f0b8e2", "#f7fabe"],
        ["#cb4804", "#7bdb4a", "#1f2cc7", "#4b94eb", "#acf9dc"],
        ["#ee04c0", "#fbbc05", "#ac4d4a", "#8ba42a", "#620206"],
        ["#a35c9c", "#f5f4d8", "#3b3817", "#ec7c6b", "#f7c523"],
        ["#15fb9b", "#2ea9df", "#3e2bb6", "#c05814", "#0f0336"],
        ["#aec71b", "#a409a1", "#8e8458", "#ea1be8", "#290227"],
        ["#b68227", "#b1dd40", "#a30b0d", "#eb2a82", "#eefdf8"],
        ["#5329f9", "#b4f731", "#267932", "#19cb8e", "#1004b8"],
        ["#b69991", "#140cbd", "#66ef2a", "#2c5b85", "#3a8e06"],
        ["#f24aba", "#e7a6e8", "#f52615", "#fdedd0", "#a60824"],
        ["#fb6e63", "#74164e", "#b0ade3", "#ca2d4a", "#886691"],
        ["#29151e", "#25f62b", "#867e00", "#2b5d37", "#30b971"],
        ["#eab052", "#0f411d", "#795837", "#8687ed", "#f9e54f"],
        ["#2f31cc", "#df5493", "#939cc0", "#5ce9ef", "#160e5d"],
        ["#4a14a1", "#d48049", "#1e5f0d", "#55727d", "#f6c4e5"],
        ["#453fff", "#b28ceb", "#9af901", "#936d24", "#3b1588"],
        ["#6c4563", "#f05ae7", "#bbb1a2", "#efe38e", "#1f1582"],
        ["#256a4a", "#cfd48a", "#28af4b", "#d501bc", "#15023e"],
        ["#237228", "#f39e38", "#7c1d2a", "#ee4af8", "#a4ddcc"],
        ["#5492e3", "#65fcf9", "#1c1a75", "#616b2e", "#03e681"],
        ["#264d0f", "#ae8441", "#2f74ef", "#fceaf1", "#52ec1c"],
        ["#e9eced", "#94c0a9", "#240fce", "#484ac2", "#468da0"],
        ["#06a67b", "#f2b34c", "#7309e7", "#506204", "#f7e6b3"],
        ["#888c42", "#cbc543", "#a706a1", "#ff29e0", "#edf38f"],
        ["#6db8f7", "#bf0c37", "#245c87", "#5d981c", "#d9f64a"],
        ["#a20fc6", "#cdc192", "#9c949c", "#297971", "#51034b"],
        ["#2fe270", "#3b2a11", "#434eec", "#3d8b3d", "#9cfbfc"],
        ["#8f5dc1", "#59af4e", "#650ee7", "#c5e14c", "#5a4977"],
        ["#5e3192", "#85c564", "#799582", "#dff682", "#3479c5"],
        ["#30d9e5", "#1e3d92", "#10174b", "#247fd9", "#f5e65a"],
        ["#b8d6da", "#b876eb", "#ad5113", "#001c20", "#a518b2"],
        ["#8b4c6d", "#967b19", "#bbd35c", "#691f1e", "#a29e66"],
        ["#28573e", "#2ea33a", "#dbe591", "#1c054e", "#6cbfac"],
        ["#66f5ed", "#a55271", "#e808b5", "#c39b6e", "#220e0d"],
        ["#b29463", "#d7302a", "#ace0e6", "#5208a2", "#377bfb"],
        ["#e09cc9", "#6a5896", "#ff0444", "#f1e924", "#ea58ea"],
        ["#626455", "#9dcb85", "#8073ee", "#5517a5", "#c1f9d3"]
    ],
    6: [
        ["#e720b9", "#74718d", "#9fc12d", "#c673f8", "#eaff62", "#3e0232"],
        ["#a69a62", "#b1c6b1", "#791a3a", "#07843d", "#eeeff1", "#04024d"],
        ["#33a11d", "#1b158a", "#e1ae3a", "#247d2e", "#cbf30b", "#882a76"],
        ["#d467c7", "#0513bf", "#05fdef", "#3c5e99", "#024d53", "#fafe83"],
        ["#a54b57", "#10cd5b", "#243bb9", "#491123", "#cee66e", "#8c75bb"],
        ["#72d3da", "#182b1c", "#366b6a", "#6ea596", "#637bc3", "#f2fa9d"],
        ["#3e2d4b", "#3fc89f", "#15082e", "#097135", "#0da22c", "#6efce6"],
        ["#79e610", "#273d86", "#e8799b", "#975d06", "#c1fae5", "#0e0381"],
        ["#76696b", "#bdca41", "#fbfb6c", "#2743a4", "#b47ca8", "#0e11a5"],
        ["#2391bf", "#514a1f", "#1f019c", "#99e81a", "#a29c6c", "#ffff80"],
        ["#4a1be8", "#36fa91", "#3cb5e8", "#834adf", "#3d8bab", "#070294"],
        ["#7e77c1", "#141f4d", "#fdcb08", "#5e518d", "#27c182", "#eefdc1"],
        ["#abb925", "#3d261a", "#f4fd76", "#9e46c4", "#b270ab", "#050113"],
        ["#cd4fb1", "#65decc", "#b00ccc", "#1c1464", "#f68023", "#e6f6ce"],
        ["#0b4fb4", "#7bcedb", "#f96d9b", "#8155f9", "#2a1421", "#fffdeb"],
        ["#c9f8bf", "#47b135", "#0e631f", "#40ec01", "#1904a0", "#677185"],
        ["#792511", "#6778ba", "#33bb85", "#f5b2ea", "#fb3706", "#1002dc"],
        ["#63c4f2", "#cdfff0", "#672b09", "#199e0f", "#045ff3", "#2c1002"],
        ["#146234", "#49bf8b", "#eaca4d", "#00045e", "#577fc9", "#113d08"],
        ["#4b9003", "#38365b", "#a2e6f9", "#52ace9", "#963ecd", "#1300c1"],
        ["#e05c1e", "#bc226b", "#c9af92", "#d9eba0", "#33261f", "#46a1dd"],
        ["#922035", "#cba397", "#3b61a8", "#0d06a5", "#7573f1", "#f5d787"],
        ["#f23c35", "#90e5df", "#622657", "#30002d", "#a1abcc", "#0eb65b"],
        ["#87b814", "#abf965", "#1f2780", "#176ab5", "#58923e", "#000038"],
        ["#ce4a0a", "#98d031", "#e064aa", "#b61c5f", "#0d0d92", "#8cfeec"],
        ["#a441ba", "#11e1be", "#e80f0e", "#310f35", "#daee70", "#6f9f09"],
        ["#68abe5", "#0b689b", "#f2ddce", "#a7757c", "#0c09e2", "#fd0410"],
        ["#523854", "#b56fcb", "#6f7028", "#a4f008", "#54c96a", "#1408f5"],
        ["#0c386a", "#c7afae", "#306351", "#b37d2e", "#bef6db", "#05097f"],
        ["#ca9e6c", "#e336e8", "#5f13c2", "#aff3d3", "#32a90a", "#0f0836"],
        ["#669aa2", "#931390", "#41cfce", "#ec5339", "#d8f89b", "#051517"],
        ["#05805a", "#dcee5e", "#763a28", "#18235b", "#2fd0ae", "#7486f2"],
        ["#3cb2d5", "#20928e", "#a2fed3", "#9b1e97", "#430f47", "#356c58"],
        ["#d1653e", "#8018b4", "#a8c3ea", "#82a191", "#37065d", "#6e47ee"],
        ["#2a5266", "#49ce78", "#7c932b", "#4b1581", "#367d70", "#a8f5d4"],
        ["#26c905", "#f33a7c", "#612ff8", "#092b70", "#98d962", "#c0fcfc"],
        ["#ccfab0", "#0c34a0", "#7eb4ea", "#a75c49", "#918b94", "#1a110a"],
        ["#f76ad3", "#d52f61", "#90d446", "#931f18", "#02113a", "#defe8a"],
        ["#a61899", "#de8f7c", "#c3e065", "#897940", "#4f0c0c", "#1b7162"],
        ["#d36ce7", "#3c30ff", "#6ef532", "#ed4148", "#410a30", "#fffeb5"],
        ["#0eab04", "#e2ebf6", "#88b95f", "#d03460", "#6c1e81", "#130360"],
        ["#4bba71", "#c00500", "#efe34f", "#4069e0", "#773c6f", "#140006"],
        ["#43eaf4", "#4ab585", "#7f5ed9", "#692da4", "#7e0119", "#f9f8ce"],
        ["#47d8f0", "#518d04", "#e0044f", "#93467a", "#09c665", "#eff9a4"],
        ["#292bfc", "#aa4b03", "#e0659b", "#f1f328", "#160957", "#7ccaa6"],
        ["#22a212", "#67dee7", "#4724fe", "#1e7295", "#001c20", "#08ce4b"],
        ["#e8772c", "#333dc5", "#59d2b2", "#dff875", "#436f7c", "#00165e"],
        ["#0fb1d9", "#78309e", "#0703b4", "#e5bc07", "#0f804b", "#f9f161"],
        ["#b92511", "#12dbd9", "#747572", "#f0fe95", "#1112f5", "#908da5"],
        ["#466367", "#6cd3e7", "#d47068", "#4a0298", "#fcee97", "#083fda"],
        ["#8ae23f", "#795cb4", "#af73f8", "#5b3a66", "#07051b", "#ccfede"],
        ["#cafbec", "#303304", "#ac984e", "#6dd7d8", "#83658c", "#6639d8"],
        ["#003b70", "#9145f7", "#cb9ac6", "#92eba0", "#b86efe", "#0b0931"],
        ["#547829", "#b7cba7", "#1e5620", "#07b8dd", "#2e1017", "#e2fef8"],
        ["#bfcaf2", "#0f7ee2", "#bb0ec5", "#7bb921", "#4c023e", "#fefda9"],
        ["#abccb1", "#56a88d", "#003551", "#4e7fa8", "#b02ea4", "#f7fe67"],
        ["#435f50", "#eef0e1", "#28a284", "#8e0d6f", "#b7b126", "#0c062b"],
        ["#419336", "#c6b4e0", "#570769", "#683e0d", "#e1f397", "#6ab01e"],
        ["#fc8bc2", "#565ad9", "#b8100c", "#eefd3d", "#280302", "#c0714d"],
        ["#8d9417", "#f1a3b8", "#504234", "#8e56be", "#54020d", "#f7f1f7"],
        ["#d90518", "#dfc3fb", "#815bba", "#7a8ec7", "#1a0332", "#f7fefa"],
        ["#5c7c7e", "#83f71d", "#6bb98d", "#d127eb", "#a80e04", "#140518"],
        ["#1da748", "#b43ee7", "#7cd926", "#1003e7", "#2b3a5b", "#f9ea82"],
        ["#e8b0f7", "#d00d1f", "#f226fc", "#76ae1e", "#2b065b", "#f3f8a1"],
        ["#46df85", "#068780", "#1b9cfa", "#d809bd", "#2f1b0c", "#eaf4cd"],
        ["#01822d", "#5d85de", "#a81c56", "#e2f543", "#95a4fa", "#0b0905"],
        ["#f4a31c", "#18a5d2", "#daef25", "#6e10f1", "#a33f9b", "#150946"],
        ["#4518c0", "#2af68c", "#bd3966", "#d959ca", "#66b713", "#050149"],
        ["#d6a8b5", "#b432c9", "#a28473", "#2e3740", "#88fbfe", "#0c0200"],
        ["#b40749", "#107d6f", "#0eff73", "#e67e8c", "#c0fff8", "#02036c"],
        ["#f30fc6", "#907e72", "#741b17", "#fab3ff", "#31cb4e", "#ecffc9"],
        ["#854ae2", "#bc8957", "#1a120c", "#482ea4", "#c6ed55", "#d0a1f9"],
        ["#dd4464", "#57d6ee", "#2324d4", "#28b324", "#c5fe82", "#18030c"],
        ["#9faf82", "#376b9d", "#68fae6", "#932151", "#2da196", "#1b07e5"],
        ["#62b7a1", "#dd5c30", "#255ab9", "#60fed0", "#3e2c32", "#1d0056"],
        ["#ba16b4", "#9275a6", "#b9b89a", "#d04908", "#230544", "#ede1ab"],
        ["#5a2981", "#9ef6ee", "#1994bd", "#107a60", "#2a0f03", "#0ef829"],
        ["#39713c", "#01a7b9", "#42ef1f", "#1b2a6a", "#d4fc67", "#080101"],
        ["#70e95e", "#43866e", "#1f00d9", "#a79838", "#214a53", "#fdf7c9"],
        ["#6e3c3a", "#fc889e", "#4dfaf3", "#407a2f", "#280aa2", "#a16fec"],
        ["#605534", "#1fd221", "#affa4b", "#64273e", "#8465f5", "#101145"],
        ["#c84437", "#5ae798", "#5b230c", "#76978b", "#e9f6d6", "#060066"],
        ["#e02e03", "#e1ecd8", "#6ed298", "#9d7549", "#272842", "#ce7fd7"],
        ["#df2c76", "#eff820", "#362bb8", "#00cf5a", "#1392c0", "#5b0016"],
        ["#5bedd8", "#fb5058", "#894623", "#be061a", "#66b1f2", "#0c0824"],
        ["#ac7834", "#ceb775", "#3d432e", "#850000", "#ece5aa", "#306e97"],
        ["#aa48e5", "#fa87cd", "#a41316", "#0d0c4f", "#06a4a2", "#65fd03"],
        ["#ef557a", "#860fec", "#edff59", "#80d3e0", "#98a462", "#1b6e1f"],
        ["#220229", "#55fe77", "#a04815", "#8f9120", "#73155e", "#4cc3a2"],
        ["#060864", "#15caa4", "#a24787", "#e8f7ef", "#024b1f", "#ca63be"],
        ["#028b17", "#23453a", "#14ea12", "#4b88e8", "#95f3da", "#06014f"],
        ["#1369e1", "#818168", "#b01098", "#16f7f6", "#0f1351", "#05d757"],
        ["#f76907", "#f2ba18", "#734102", "#6c0986", "#6d58dd", "#d1fc8a"],
        ["#6b634f", "#129cb5", "#a82d16", "#3ae8a8", "#d1f7fc", "#29050d"],
        ["#e8c6cc", "#3b28b1", "#4d806d", "#38589b", "#d7864d", "#1c0b29"],
        ["#c42eb2", "#d88e14", "#efc440", "#0c2d5e", "#c352fa", "#f5f5c4"],
        ["#c762fa", "#bf4987", "#1be1df", "#f2fcf1", "#1f571e", "#012d43"],
        ["#0d6e26", "#b9032a", "#b1a91c", "#6c80da", "#24f7bf", "#fafcae"],
        ["#2c47ee", "#55ad62", "#94cac2", "#2b283c", "#2b7999", "#dceed1"],
        ["#fab4c7", "#0b3de5", "#c04346", "#ada12a", "#2790ab", "#1d120b"]
    ],
    7: [
        ["#d1603f", "#92d4b9", "#170256", "#4d226b", "#b03873", "#b5898d", "#fcf5b0"],
        ["#807ac6", "#69dae1", "#cd0362", "#f324ef", "#edfc69", "#2b0b09", "#cb9d2b"],
        ["#4727b4", "#a38a53", "#e42b50", "#cde9c3", "#f1a24f", "#357bc7", "#151335"],
        ["#3f30c2", "#2db847", "#904c60", "#c7fce8", "#3beb4a", "#030c65", "#2e889a"],
        ["#e9f4dc", "#eb64cf", "#0eea7f", "#033367", "#f54910", "#8e2f9f", "#170201"],
        ["#e81a08", "#8ed6e4", "#7b5d77", "#2c9f45", "#1118d8", "#879dfb", "#fffbf1"],
        ["#2873e5", "#2b2970", "#0aaff9", "#d5fb57", "#0d0320", "#a8b5d0", "#8e3a6c"],
        ["#f15afc", "#e82239", "#e7e78e", "#0825ef", "#c0a88a", "#170321", "#5e7819"],
        ["#386ab6", "#f0bbd6", "#ae1904", "#be738e", "#0f05ee", "#0fc8ec", "#f3feae"],
        ["#81d3a0", "#576322", "#5c7aa8", "#482f15", "#21bb4d", "#baff9a", "#050167"],
        ["#6519f0", "#88db80", "#e981bb", "#3e6853", "#ccfae8", "#a46bb0", "#140952"],
        ["#969d64", "#217543", "#cbfba2", "#ba00e5", "#51de9e", "#638a18", "#1d0875"],
        ["#5681a8", "#a4d478", "#4d6c1b", "#742f3b", "#e68a86", "#21170b", "#d6fffa"],
        ["#a2cde3", "#f53aa9", "#183038", "#549f10", "#1a5f32", "#fdf3ea", "#0e010b"],
        ["#781a3e", "#07cd3f", "#daf770", "#d125ba", "#ac6c75", "#7dcebe", "#10040c"],
        ["#916db3", "#ebafa5", "#151347", "#8c5434", "#fcfa0c", "#9c9c6e", "#02468a"],
        ["#700ebd", "#cf4ba0", "#908dac", "#e6efb6", "#1ee96f", "#240126", "#b2314a"],
        ["#05bef9", "#745585", "#ddd54c", "#7e10f4", "#9e7837", "#0e0266", "#fcfeed"],
        ["#8e94bf", "#07f69a", "#036e2b", "#5b194f", "#677d50", "#ecf939", "#030202"],
        ["#02080b", "#545104", "#5dea82", "#4fa885", "#8c5e83", "#5a11ba", "#f6f8f4"],
        ["#6975d5", "#ff1863", "#2e1bc5", "#4aaf89", "#3bf5a0", "#d9ffe8", "#000124"],
        ["#6648bc", "#34a6ae", "#1521d8", "#c5e9d3", "#bbafde", "#d85e13", "#06021a"],
        ["#70a566", "#96028a", "#846781", "#a9ced0", "#e92317", "#eaffa3", "#040133"],
        ["#303926", "#c622fb", "#06efb7", "#3f9eed", "#548134", "#e5f0f1", "#1e040d"],
        ["#b3d498", "#f016d7", "#59777a", "#f57d55", "#03397e", "#1d0c02", "#d5ffff"],
        ["#e2b2d2", "#d95223", "#5e4b3a", "#828e6e", "#1527a5", "#e9f973", "#1b000a"],
        ["#342dad", "#7fe4a7", "#b63af5", "#56c056", "#7e842f", "#630401", "#e5ffe9"],
        ["#859ede", "#07216e", "#b54745", "#12fbbb", "#21977f", "#8c2957", "#fbf89d"],
        ["#379c29", "#030617", "#ec0340", "#9be75d", "#9b98bb", "#d125da", "#f3ffef"],
        ["#74ea8b", "#4d10f1", "#63484a", "#6293fc", "#4c804e", "#070615", "#e9fee6"],
        ["#a53cf5", "#59f32c", "#322e6c", "#7e74dd", "#030579", "#e28d72", "#f7feb9"],
        ["#420052", "#f87c8b", "#89e487", "#b94325", "#4185b7", "#502c97", "#f1f8f1"],
        ["#6b7082", "#4d18a3", "#2ae6ee", "#2aaadc", "#595048", "#f0fa7d", "#240018"],
        ["#f0c5e5", "#cc4796", "#39a37d", "#531884", "#8bbb50", "#3e40f1", "#170215"],
        ["#51945d", "#cf9e1c", "#065010", "#5af27c", "#76506c", "#041692", "#f7fad8"],
        ["#ad0f53", "#219970", "#9ed3a6", "#b34681", "#0b0f0b", "#4ea8f0", "#f1fffc"],
        ["#c94513", "#66ab73", "#76dcaf", "#2d39a3", "#0d1271", "#df5d8a", "#f7ffa6"],
        ["#931019", "#c1da32", "#2cb588", "#5b64cc", "#1d5385", "#e5fced", "#16000f"],
        ["#3364e8", "#c69790", "#51ebeb", "#bd037b", "#27050f", "#6785b8", "#f4fbf7"],
        ["#d78903", "#856a98", "#a31433", "#1b6b22", "#a4dd56", "#270c35", "#fffec5"],
        ["#09f4b8", "#e48759", "#af0d8b", "#e4f2ea", "#4c8498", "#f62f21", "#051f0a"],
        ["#130311", "#a0190a", "#0df4f7", "#c757f3", "#42bba8", "#793dce", "#dafccb"],
        ["#d59e46", "#8754cb", "#85f30e", "#9a174d", "#648897", "#0c0f15", "#f4fee9"],
        ["#2c74fa", "#09dfa8", "#930c5b", "#c8e7de", "#f16f7c", "#f82130", "#070a19"],
        ["#9d946b", "#8a5afd", "#3e5589", "#1c3539", "#b3c16d", "#d9f6aa", "#1b0428"],
        ["#f1d30b", "#5c207e", "#e023df", "#988030", "#bc94eb", "#24012b", "#f3febf"],
        ["#b59e39", "#aa181d", "#acde63", "#31028f", "#6948f6", "#916ca1", "#fdf5fe"],
        ["#22259d", "#aed5b9", "#7fa05a", "#4a5800", "#2985df", "#19040f", "#f8fdc0"],
        ["#76f707", "#b53550", "#80103f", "#26b73d", "#1084ef", "#0e0115", "#fafeef"],
        ["#957d09", "#95c884", "#142b9d", "#7048c9", "#b5fe54", "#50a1f5", "#070a0d"],
        ["#68257b", "#925439", "#37f1b5", "#171731", "#7a7d8d", "#9fa438", "#f7fe71"],
        ["#853e5d", "#6cbc9f", "#93160c", "#a654a4", "#97f5b8", "#db69c2", "#070560"],
        ["#f7802f", "#7009ed", "#bbb4fe", "#b8f1ef", "#87466b", "#8c679d", "#17005a"],
        ["#b16dd0", "#0209aa", "#c62ef7", "#dec7bc", "#583178", "#d5a305", "#edfefe"],
        ["#f0c1d7", "#44927a", "#2e3345", "#3563fb", "#f885e2", "#01008e", "#fffbe5"],
        ["#968464", "#40fc8b", "#bd3272", "#6c1c0f", "#f49a2d", "#08002c", "#f5fff7"],
        ["#2f2d12", "#dc873f", "#a3fc7b", "#856f6f", "#e719d5", "#c0afda", "#1b0003"],
        ["#c34646", "#49e384", "#7a1d95", "#69a59b", "#d2ff24", "#826ee0", "#4f0265"],
        ["#032bc2", "#15661d", "#9b868c", "#f3cf9e", "#3e73c8", "#e1a45d", "#090402"],
        ["#72ea64", "#70330f", "#f746d7", "#3a03b8", "#b49529", "#6b594a", "#fdf6e8"],
        ["#0c5eca", "#880e66", "#9187e0", "#cbd12e", "#d55e2a", "#090016", "#f8fa8a"],
        ["#a74e57", "#d80c5b", "#7fac53", "#a5e137", "#489143", "#450b1a", "#f4ffb8"],
        ["#6b8f49", "#99df8d", "#b84204", "#681a5d", "#230611", "#3cb9d9", "#fefcf6"],
        ["#d71d74", "#5daff9", "#ca68c1", "#c0c6e8", "#1e057b", "#8355e7", "#f5fe94"],
        ["#27896b", "#52de8e", "#940ea6", "#409de0", "#316323", "#fdf7c5", "#2a0924"],
        ["#041024", "#f870c7", "#59fe1a", "#344aef", "#1b8f30", "#323804", "#fefe9e"],
        ["#94a685", "#2f4b8a", "#516e65", "#81e890", "#000ad5", "#39949e", "#effdf1"],
        ["#3ed8a8", "#000c9b", "#5c48ac", "#e4ed90", "#41351a", "#2ea77d", "#8d6586"],
        ["#0f25ab", "#d85702", "#8aaf9b", "#4df7a3", "#35593d", "#f8fde5", "#a279bc"],
        ["#bcffbf", "#58496b", "#929c55", "#de597b", "#51dcb5", "#b10820", "#000923"],
        ["#cb2678", "#01921e", "#35ea58", "#9e02a9", "#eb7cab", "#b1fac9", "#15060f"],
        ["#32915f", "#c0c395", "#3e4d9c", "#c686eb", "#23380c", "#fffcbc", "#050a2b"],
        ["#98e20b", "#1a9338", "#2a2486", "#0ad042", "#f5fce5", "#0656c2", "#020051"],
        ["#b2437b", "#d4dd25", "#06c7af", "#470d6c", "#113fd6", "#53960b", "#f4fff9"],
        ["#914690", "#5e19df", "#e6f2d1", "#b1bf7f", "#b061bd", "#45b53c", "#0d0d0d"],
        ["#c38855", "#c6db25", "#022ca5", "#0a6c8d", "#6670d9", "#fefbe1", "#0f011b"],
        ["#bf1843", "#94db3d", "#44973b", "#7f569e", "#3b0f09", "#a29aa6", "#f8ecd7"],
        ["#4ee12d", "#e87777", "#1d569a", "#b2035a", "#4071c8", "#eedbef", "#000609"],
        ["#eb52b1", "#dea6fe", "#a6957c", "#8613a3", "#9b2fec", "#1a073f", "#e8f787"],
        ["#97ef9c", "#b84ce3", "#53ce38", "#292940", "#075877", "#ee6c75", "#000305"],
        ["#b33700", "#7a7185", "#c0ce10", "#dbfcec", "#1a0229", "#ae87b7", "#291afc"],
        ["#7b3064", "#bbdb64", "#b6802c", "#eb90b1", "#c442f2", "#1c2716", "#f6fdfe"],
        ["#f52c35", "#4898f6", "#1cf796", "#440079", "#e7f0d8", "#2e2add", "#8a760c"],
        ["#7e4f9d", "#0dc470", "#09ebe4", "#4a295a", "#f5ff19", "#3a8e73", "#2a0344"],
        ["#19facc", "#bd0289", "#df55ff", "#297619", "#aba064", "#090646", "#fdff62"],
        ["#69a797", "#8bcead", "#236d66", "#3f22b8", "#f2fc80", "#1f9c20", "#2a0142"],
        ["#ea006a", "#a169a5", "#8ac4c6", "#e129f6", "#d5fecf", "#0f09bf", "#50b61c"],
        ["#2261ba", "#c96178", "#ebb721", "#d60667", "#a2fdd5", "#0b0a11", "#4aaa9b"],
        ["#774bb2", "#637bef", "#5becaf", "#b11956", "#2702c3", "#2ac95f", "#fcfcf7"],
        ["#4e93b4", "#fdddf2", "#b3be2a", "#1d1fd1", "#aa3056", "#cb4f69", "#170004"],
        ["#80ba88", "#db5915", "#8e34b2", "#a7f321", "#7703fd", "#798ac8", "#0f003f"],
        ["#68f51d", "#ba3b55", "#ee7e83", "#372cc3", "#210766", "#9067a6", "#fff5d0"],
        ["#b05e81", "#4e277e", "#e7b1ff", "#d0927c", "#1f0b49", "#39631f", "#e8f8ae"],
        ["#82b66c", "#b145fd", "#242866", "#93ded9", "#7c3899", "#d564d4", "#000508"],
        ["#d069fa", "#435d1a", "#55d402", "#ddfbf6", "#3914de", "#74771e", "#080207"],
        ["#aaa53d", "#303336", "#b04df4", "#ebbaaa", "#ecf8be", "#02060c", "#205c78"],
        ["#452540", "#0c8b66", "#23cbbb", "#c3e767", "#7935dd", "#b28335", "#0f024a"],
        ["#62273e", "#36b5a9", "#f62a83", "#87e959", "#9b743d", "#260273", "#eefddb"],
        ["#985821", "#1fd445", "#a8d896", "#372770", "#089be8", "#0b091b", "#fcfff5"],
        ["#464fd9", "#3e0087", "#989eb1", "#c20a54", "#28eee5", "#2e8497", "#f8f6b4"]
    ],
    8: [
        ["#000000", "#0020fb", "#0052b9", "#0074fa", "#009cd6", "#00c2fd", "#00fe9e", "#a6fffe"]
    ]
};

let currentNumColors = 3;
let currentPalette = [];

// Color conversion functions
function hexToRgb(hex) {
    hex = hex.replace(/^#/, '');
    return {
        r: parseInt(hex.substring(0, 2), 16),
        g: parseInt(hex.substring(2, 4), 16),
        b: parseInt(hex.substring(4, 6), 16)
    };
}

function rgbToHex(rgb) {
    return "#" + 
        Math.round(rgb.r).toString(16).padStart(2, '0') + 
        Math.round(rgb.g).toString(16).padStart(2, '0') + 
        Math.round(rgb.b).toString(16).padStart(2, '0');
}

function normalizeRgb(rgb) {
    return {
        r: rgb.r / 255.0,
        g: rgb.g / 255.0,
        b: rgb.b / 255.0
    };
}

function denormalizeRgb(rgb) {
    return {
        r: Math.min(255, Math.max(0, rgb.r * 255)),
        g: Math.min(255, Math.max(0, rgb.g * 255)),
        b: Math.min(255, Math.max(0, rgb.b * 255))
    };
}

function convertToProtanopia(hex) {
    const rgb = normalizeRgb(hexToRgb(hex));
    
    // Transformation matrix for protanopia (Machado et al.)
    const simMatrix = [
        [0.152286, 1.052583, -0.204868],
        [0.114503, 0.786281, 0.099216],
        [-0.003882, -0.048116, 1.051998]
    ];
    
    const simulatedRgb = {
        r: simMatrix[0][0] * rgb.r + simMatrix[0][1] * rgb.g + simMatrix[0][2] * rgb.b,
        g: simMatrix[1][0] * rgb.r + simMatrix[1][1] * rgb.g + simMatrix[1][2] * rgb.b,
        b: simMatrix[2][0] * rgb.r + simMatrix[2][1] * rgb.g + simMatrix[2][2] * rgb.b
    };
    
    return rgbToHex(denormalizeRgb(simulatedRgb));
}

function convertToDeuteranopia(hex) {
    const rgb = normalizeRgb(hexToRgb(hex));
    
    // Transformation matrix for deuteranopia (Machado et al.)
    const simMatrix = [
        [0.367322, 0.860646, -0.227968],
        [0.280085, 0.672501, 0.047413],
        [-0.011820, 0.042940, 0.968881]
    ];
    
    const simulatedRgb = {
        r: simMatrix[0][0] * rgb.r + simMatrix[0][1] * rgb.g + simMatrix[0][2] * rgb.b,
        g: simMatrix[1][0] * rgb.r + simMatrix[1][1] * rgb.g + simMatrix[1][2] * rgb.b,
        b: simMatrix[2][0] * rgb.r + simMatrix[2][1] * rgb.g + simMatrix[2][2] * rgb.b
    };
    
    return rgbToHex(denormalizeRgb(simulatedRgb));
}

function convertToTritanopia(hex) {
    const rgb = normalizeRgb(hexToRgb(hex));
    
    // Transformation matrix for tritanopia (Machado et al.)
    const simMatrix = [
        [1.255528, -0.076749, -0.178779],
        [-0.078411, 0.930809, 0.147602],
        [0.004733, 0.691367, 0.303900]
    ];
    
    const simulatedRgb = {
        r: simMatrix[0][0] * rgb.r + simMatrix[0][1] * rgb.g + simMatrix[0][2] * rgb.b,
        g: simMatrix[1][0] * rgb.r + simMatrix[1][1] * rgb.g + simMatrix[1][2] * rgb.b,
        b: simMatrix[2][0] * rgb.r + simMatrix[2][1] * rgb.g + simMatrix[2][2] * rgb.b
    };
    
    return rgbToHex(denormalizeRgb(simulatedRgb));
}

function convertToGreyScale(hex) {
    const rgb = hexToRgb(hex);
    const grey = Math.round(0.2126 * rgb.r + 0.7152 * rgb.g + 0.0722 * rgb.b);
    return `#${grey.toString(16).padStart(2, '0')}${grey.toString(16).padStart(2, '0')}${grey.toString(16).padStart(2, '0')}`;
}

// Get a random palette
function getRandomPalette(numColors) {
    const palettes = allPalettes[numColors];
    
    const randomIndex = Math.floor(Math.random() * palettes.length);
    console.log(`Palette chosen: index ${randomIndex} from ${palettes.length} palettes`);
    return palettes[randomIndex];
}

// Generate a random palette
function generateRandomPalette() {
    // Check if 8-color palette and random is disabled
    if (currentNumColors === 8 && allPalettes[8].length <= 1) {
        console.log("Random button disabled for 8-color palettes");
        // Still show the first palette for 8 colors
        currentPalette = allPalettes[8][0];
        updateDisplays();
        return;
    }
    
    try {
        currentPalette = getRandomPalette(currentNumColors);
        updateDisplays();
        // Hide error message if all goes well
        document.getElementById('error-message').style.display = 'none';
    } catch (error) {
        console.error("Error generating random palette:", error);
        // Show error message
        document.getElementById('error-message').style.display = 'block';
    }
}

// Update the randomize button state
function updateRandomizeButtonState() {
    const randomButton = document.getElementById('random-palette');
    const infoMessage = document.getElementById('wip-message');
    
    if (currentNumColors === 8 && allPalettes[8].length <= 1) {
        // Disable the button
        randomButton.classList.add('disabled');
        // Show the message
        infoMessage.style.display = 'block';
    } else {
        // Enable the button
        randomButton.classList.remove('disabled');
        // Hide the message
        infoMessage.style.display = 'none';
    }
}

// Update displays
function updateDisplays() {
    // Check if palette is valid
    if (!currentPalette || currentPalette.length === 0) {
        console.error("Empty or undefined palette");
        document.getElementById('error-message').style.display = 'block';
        return;
    }
    
    console.log("Updating displays with palette:", currentPalette);
    
    // Update color wheels
    updateColorWheel('normal-wheel', currentPalette);
    
    // For different vision types
    updateColorWheel('protanopia-wheel', currentPalette.map(convertToProtanopia));
    updateColorWheel('deuteranopia-wheel', currentPalette.map(convertToDeuteranopia));
    updateColorWheel('tritanopia-wheel', currentPalette.map(convertToTritanopia));
    updateColorWheel('grey-scale-wheel', currentPalette.map(convertToGreyScale));
    
    // Update HEX codes display
    document.getElementById('hex-codes').textContent = currentPalette.join(', ');
}

// Create color wheel segments
function updateColorWheel(wheelId, colors) {
    const wheel = document.getElementById(wheelId);
    if (!wheel) {
        console.error(`Element #${wheelId} not found`);
        return;
    }
    
    wheel.innerHTML = '';
    
    const numColors = colors.length;
    if (numColors === 0) {
        console.error("No colors provided for the wheel");
        return;
    }
    
    // Create SVG element for the wheel
    const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
    svg.setAttribute("width", "100%");
    svg.setAttribute("height", "100%");
    svg.setAttribute("viewBox", "0 0 100 100");
    svg.style.position = "absolute";
    svg.style.top = "0";
    svg.style.left = "0";
    
    // Create wheel segments with SVG
    const centerX = 50;
    const centerY = 50;
    const outerRadius = 50;
    const innerRadius = 20;  // For the center hole
    const angleStep = 360 / numColors;
    
    colors.forEach((color, i) => {
        // Check that the color is valid
        if (!color || color === "") {
            console.error(`Invalid color at index ${i}`);
            return;
        }
        
        const startAngle = i * angleStep;
        const endAngle = (i + 1) * angleStep;
        
        // Calculate SVG path points
        const startRad = (startAngle - 90) * Math.PI / 180;
        const endRad = (endAngle - 90) * Math.PI / 180;
        
        const x1 = centerX + innerRadius * Math.cos(startRad);
        const y1 = centerY + innerRadius * Math.sin(startRad);
        const x2 = centerX + outerRadius * Math.cos(startRad);
        const y2 = centerY + outerRadius * Math.sin(startRad);
        const x3 = centerX + outerRadius * Math.cos(endRad);
        const y3 = centerY + outerRadius * Math.sin(endRad);
        const x4 = centerX + innerRadius * Math.cos(endRad);
        const y4 = centerY + innerRadius * Math.sin(endRad);
        
        // Create SVG path for the segment
        const path = document.createElementNS("http://www.w3.org/2000/svg", "path");
        const largeArcFlag = endAngle - startAngle <= 180 ? "0" : "1";
        
        const d = [
            `M ${x1},${y1}`,
            `L ${x2},${y2}`,
            `A ${outerRadius},${outerRadius} 0 ${largeArcFlag} 1 ${x3},${y3}`,
            `L ${x4},${y4}`,
            `A ${innerRadius},${innerRadius} 0 ${largeArcFlag} 0 ${x1},${y1}`,
            `Z`
        ].join(" ");
        
        path.setAttribute("d", d);
        path.setAttribute("fill", color);
        
        svg.appendChild(path);
    });
    
    // Add SVG to the wheel
    wheel.appendChild(svg);
}

// Event Listeners
// Copy HEX codes to clipboard without alerts
document.getElementById('copy-button').addEventListener('click', function(e) {
    e.preventDefault();
    const hexText = document.getElementById('hex-codes').textContent;
    navigator.clipboard.writeText(hexText).then(() => {
        // Subtle visual feedback instead of alert
        const button = this;
        const originalText = button.textContent;
        button.textContent = "COPIED!";
        button.style.backgroundColor = "#4CAF50"; // Green to indicate success
        
        // Return to original state after 1 second
        setTimeout(() => {
            button.textContent = originalText;
            button.style.backgroundColor = "";
        }, 1000);
    }).catch(err => {
        console.error('Error copying:', err);
        // Visual feedback for error, still no alert
        const button = this;
        button.textContent = "ERROR";
        button.style.backgroundColor = "#F44336"; // Red to indicate error
        
        // Return to original state after 1 second
        setTimeout(() => {
            button.textContent = "COPY";
            button.style.backgroundColor = "";
        }, 1000);
    });
});

// Change the number of colors
document.getElementById('color-selector').addEventListener('click', function(e) {
    e.preventDefault();
    currentNumColors = currentNumColors < 8 ? currentNumColors + 1 : 3;
    this.textContent = `Number of colors : ${currentNumColors}`;
    
    // Update the random button state when changing color number
    updateRandomizeButtonState();
    
    generateRandomPalette();
});

// Generate a random palette on click
document.getElementById('random-palette').addEventListener('click', function(e) {
    e.preventDefault();
    // Only generate if the button is not disabled
    if (!this.classList.contains('disabled')) {
        generateRandomPalette();
    }
});

// Initialization
document.addEventListener('DOMContentLoaded', function() {
    console.log("Initializing application...");
    document.getElementById('color-selector').textContent = `Number of colors : ${currentNumColors}`;
    
    // Initial state of the random button
    updateRandomizeButtonState();
    
    generateRandomPalette();
}); 